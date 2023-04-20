import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import NoReverseMatch, reverse
from seo.models import SeoPage
from content_app.models import Post
from django.conf import settings
import xml.etree.cElementTree as ET

def init_sitemap_file(request):
    if request.user.is_authenticated and request.user.is_superuser:
        root = ET.Element('urlset')
        root.attrib['xmlns:xsi']="http://www.w3.org/2001/XMLSchema-instance"
        root.attrib['xsi:schemaLocation']="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
        root.attrib['xmlns']="http://www.sitemaps.org/schemas/sitemap/0.9"
        dt = datetime.datetime.now().strftime ("%Y-%m-%d")
        # seo pages
        pages = SeoPage.objects.all()
        for page in pages:
            try:
                doc = ET.SubElement(root, "url")
                ET.SubElement(doc, "loc").text = settings.SITE_URL + reverse(page.page)
                ET.SubElement(doc, "lastmod").text = dt
                ET.SubElement(doc, "changefreq").text = "weekly"
                ET.SubElement(doc, "priority").text = "1.0"
            except NoReverseMatch:
                print(f"Error for page - {page.page}")
        # seo posts
        posts = Post.objects.all()
        for post in posts:
            try:
                doc = ET.SubElement(root, "url")
                ET.SubElement(doc, "loc").text = settings.SITE_URL + reverse("post", args=(post.slug,))
                ET.SubElement(doc, "lastmod").text = dt
                ET.SubElement(doc, "changefreq").text = "weekly"
                ET.SubElement(doc, "priority").text = "0.9"
            except NoReverseMatch:
                print(f"Error for page - {post.slug}")

        tree = ET.ElementTree(root)
        tree.write('static/sitemap.xml', encoding='utf-8', xml_declaration=True)
        return HttpResponse(open('static/sitemap.xml').read(), content_type='text/xml')
    else:
        return HttpResponse("You haven`t permissions!")
