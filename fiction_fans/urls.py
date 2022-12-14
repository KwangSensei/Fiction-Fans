from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import (
    HomePage,
    Profile,
    HotPage,
    RecentlyPage,
    ChapterView,
    fiction_view,
    create_chapter,
    create_fiction,
    edit_fiction,
    edit_chapter,
    delete_chapter,
    delete_fiction,
    comment,
    rate,
    upload_image_view,
)


app_name = "fiction_fans"
urlpatterns = [
    path("", HomePage.as_view(), name="homepage"),

    path("user/", Profile.as_view(), name="profile"),

    path("<int:fiction_id>/", fiction_view, name="fiction_view"),

    path("createfic/", create_fiction, name="fiction_create"),

    path("<int:fiction_id>/edit/", edit_fiction, name="fiction_edit"),

    path("<int:fiction_id>/del/", delete_fiction, name="fiction_del"),

    path(
        "<int:fiction_pk>/<int:chapter_pk>/",
        ChapterView.as_view(),
        name="chapter_view"
    ),

    path(
        "<int:fiction_pk>/createchap/",
        create_chapter,
        name="chapter_create"
    ),

    path(
        "<int:fiction_id>/<int:chapter_id>/edit/",
        edit_chapter,
        name="chapter_edit"
    ),

    path(
        "<int:fiction_id>/<int:chapter_id>/del/",
        delete_chapter,
        name="chapter_del"
    ),

    path(
        "<int:fiction_pk>/<int:chapter_pk>/comment/",
        comment,
        name="chapter_comment"
    ),

    path("hot/", HotPage.as_view(), name="hot_index"),

    path("recently/", RecentlyPage.as_view(), name="recently_index"),

    path(
        "<int:fiction_pk>/<int:chapter_pk>/rate/",
        rate,
        name="rate_chapter"
    ),

    path("imageUPload/", csrf_exempt(upload_image_view)),
]
