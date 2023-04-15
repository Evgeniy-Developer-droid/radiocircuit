from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator
from forum_app.models import Chapter, Topic, Message


class ForumMessagesView(View):
    template_view = 'forum_app/forum_messages.html'

    def get(self, request, chapter_slug, topic_slug):
        try:
            chapter = Chapter.objects.get(slug=chapter_slug)
            topic = Topic.objects.get(slug=topic_slug)
            instances = Message.objects.filter(chapter=chapter, topic=topic).order_by('created')
            paginator = Paginator(instances, 15)
            page_number = request.GET.get("page", 1)
            page_obj = paginator.get_page(page_number)
            page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
            get_params = dict()
            for k, v in request.GET.items():
                get_params[k] = v
            get_params.pop("page", None)
            instances = page_obj.object_list
            if 'page' not in request.GET:
                return redirect(reverse("forum_messages", args=(chapter.slug, topic.slug))+f"?page={paginator.num_pages}")
            return render(request, self.template_view, context={
                "title": f"RadioCircuit | Messages",
                "messages": instances,
                "topic": topic,
                "chapter": chapter,
                "page_obj": page_obj,
                "get_params": get_params,
            })
        except (Chapter.DoesNotExist, Topic.DoesNotExist):
            raise Http404()


class ForumTopicsView(View):
    template_view = 'forum_app/forum_topics.html'

    def get(self, request, chapter_slug):
        try:
            chapter = Chapter.objects.get(slug=chapter_slug)
            instances = Topic.objects.filter(chapter=chapter).order_by('-created')
            paginator = Paginator(instances, 15)
            page_number = request.GET.get("page", 1)
            page_obj = paginator.get_page(page_number)
            page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
            get_params = dict()
            for k, v in request.GET.items():
                get_params[k] = v
            get_params.pop("page", None)
            instances = page_obj.object_list
            return render(request, self.template_view, context={
                "title": f"RadioCircuit | Topics",
                "topics": instances,
                "chapter": chapter,
                "page_obj": page_obj,
                "get_params": get_params,
            })
        except Chapter.DoesNotExist:
            raise Http404()


class ForumChaptersView(View):
    template_view = 'forum_app/forum_chapters.html'

    def get(self, request):
        chapters = Chapter.objects.all()
        return render(request, self.template_view, context={
            "title": f"RadioCircuit | Chapters",
            "chapters": chapters
        })
