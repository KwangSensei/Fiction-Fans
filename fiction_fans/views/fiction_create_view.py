from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from ..forms.fiction_create_form import FictionForm, ChapterForm
from ..models import FictionTitle
from django.conf import settings
from . import storage

# Create your views here.


def create_fiction(request):
    """
    For creating fiction title page.
    """
    form = FictionForm(request.POST or None)
    template_name = "fiction_fans/fiction_create.html"
    context = {
        "form": form,
    }
    if request.method == "POST":
        if form.is_valid():
            fiction = form.save(commit=False)
            fiction.user = request.user
            fiction.cover_url = storage.upload(request)
            fiction.save()
            return HttpResponseRedirect(reverse("fiction_fans:fiction_view", args=(fiction.id,)))
    return render(request, template_name, context=context)


def create_chapter(request, fiction_pk):
    """
    For creating chapter in fiction title.
    """
    template_name = "fiction_fans/chapter_create.html"
    form = ChapterForm(request.POST or None)
    context = {
        "form": form,
    }
    if request.method == "POST":
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.fiction_title_id = fiction_pk
            chapter.save()
            chapter_pk = chapter.id
            return HttpResponseRedirect(reverse("fiction_fans:chapter_view", args=[fiction_pk, chapter_pk]))
    return render(request, template_name, context=context)
