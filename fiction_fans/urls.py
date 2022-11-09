from django.urls import path
from .views import homepage_view, ChapterView



app_name = "fiction_fans"
urlpatterns = [
    path("", homepage_view.HomePage.as_view(), name="homepage"),
    path("<int:fiction_id>/detail", fiction_view.fiction_view, name="fiction_view"),
    path("<int:fiction_pk>/<int:chapter_pk>/detail", ChapterView.as_view(), name="chapter_view"),
]
