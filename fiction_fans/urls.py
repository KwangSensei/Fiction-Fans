from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import (HomePage
                    , fiction_view
                    , upload_image_view
                    , create_chapter
                    , create_fiction
                    , edit_fiction
                    , edit_chapter
                    , comment
                    , ChapterView
                    , delete_chapter
                    , delete_fiction
                    , Profile)

app_name = "fiction_fans"
urlpatterns = [
    path("", HomePage.as_view(), name="homepage"),
    path("<int:fiction_id>/", fiction_view, name="fiction_view"),
    path("createfic/", create_fiction, name="fiction_create"),
    path("<int:fiction_id>/edit/", edit_fiction, name="fiction_edit"),
    path("<int:fiction_id>/del/", delete_fiction, name="fiction_del"),
    path("<int:fiction_pk>/<int:chapter_pk>/", ChapterView.as_view(), name="chapter_view"),
    path("createchap/", create_chapter, name="chapter_create"),
    path("<int:fiction_id>/<int:chapter_id>/edit/", edit_chapter, name="chapter_edit"),
    path("<int:fiction_id>/<int:chapter_id>/del/", delete_chapter, name="chapter_del"),
    path("imageUPload/", csrf_exempt(upload_image_view)),
    path("<int:fiction_pk>/<int:chapter_pk>/comment/", comment, name="chapter_comment"),
    path("user/", Profile.as_view(), name="profile"),
]
