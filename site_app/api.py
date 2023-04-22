
from django.http import HttpResponse, HttpResponseBadRequest
import json
from django.views.decorators.csrf import csrf_exempt
from content_app.models import Post, PostContent
from django.utils.text import slugify
import requests
import tempfile
from django.core import files


@csrf_exempt
def import_post(request):
    data = json.loads(request.body)
    
    if data.get('token', None) != "evgen-super-good228":
        return HttpResponseBadRequest("Permission denied!")
    
    response = requests.get(data.get("image"), stream=True)
    if response.status_code != requests.codes.ok:
        return HttpResponseBadRequest("image error link")
    file_name = data.get("image").split('/')[-1]
    lf = tempfile.NamedTemporaryFile(delete=True)
    for block in response.iter_content(1024 * 8):
        if not block:
            break
        lf.write(block)

    post = Post.objects.create(
        title=data.get("title"),
        description=data.get("description"),
        slug=slugify(data.get("title")),
        author=data.get("author")
    )
    post.image.save(file_name, files.File(lf))

    if not post.image:
        post.delete()
        return HttpResponseBadRequest("image error link")
    
    for content_item in data.get('content'):
        if content_item.get('image', None):
            response = requests.get(content_item.get("image"), stream=True)
            if response.status_code != requests.codes.ok:
                return HttpResponseBadRequest("image error link")
            file_name = content_item.get("image").split('/')[-1]
            lf = tempfile.NamedTemporaryFile(delete=True)
            for block in response.iter_content(1024 * 8):
                if not block:
                    break
                lf.write(block)
            pc = PostContent.objects.create(post=post)
            pc.image.save(file_name, files.File(lf))
            if not pc.image:
                pc.delete()
        elif content_item.get('body', None):
            pc = PostContent.objects.create(
                post=post,
                content=content_item.get("body")
            )

    return HttpResponse("OK")