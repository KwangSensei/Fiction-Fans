from django.urls import path
from .views import HomePage, ChapterView, FictionView



app_name = "fiction_fans"
urlpatterns = [
    path("", HomePage.as_view(), name="homepage"),
    path("<int:fiction_pk>/detail", FictionView.as_view(), name="fiction_view"),
    path("<int:fiction_pk>/<int:chapter_pk>/detail", ChapterView.as_view(), name="chapter_view"),
]
