from django.urls import path
from forum_app import views

urlpatterns = [
    path('chapters', views.ForumChaptersView.as_view(), name="forum_chapters"),
    path('chapter/<slug:chapter_slug>/topics', views.ForumTopicsView.as_view(), name="forum_topics"),
    path('chapter/<slug:chapter_slug>/topic/<slug:topic_slug>', views.ForumMessagesView.as_view(), name="forum_messages"),
]
