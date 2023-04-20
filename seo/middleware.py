

from seo.models import Visitor


class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        visitor_token = request.COOKIES.get('visitor_token', None)
        user = request.user.username or 'anonymus'
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        response = self.get_response(request)
        
        if not visitor_token:
            instance = Visitor.objects.create(
                user=user,
                ip=ip
            )
            response.set_cookie(
                "visitor_token",
                instance.token,
                max_age=60*60 # 1 hour
            ) 
        return response