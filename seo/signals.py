from django.db.models.signals import pre_save
from django.dispatch import receiver
from seo.models import Visitor
import requests


@receiver(pre_save, sender=Visitor)
def set_ip_location(sender, instance, *args, **kwargs):
    res = requests.get(f"https://api.iplocation.net/?ip={instance.ip}")
    data = res.json()
    if int(data.get("response_code", 400)) == 200:
        instance.country = data.get("country_name", "unknown")
        instance.country = data.get("isp", "unknown")
