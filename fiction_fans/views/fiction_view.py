"""Create view for reading fiction's story."""
from django.shortcuts import render
from ..models.fiction_model import FictionTitle, FictionChapter
from django.views import generic

# Create your views here.


class ChapterView(generic.DetailView):
    """Create view for reading fiction's chapter page."""
    template_name = "fiction_fans/chapter_page.html"
    model = FictionChapter

    def get_queryset(self):
        fiction_pk = self.kwargs.get("fiction_pk")
        return FictionTitle.objects.filter(pk=fiction_pk)

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        chapter_pk = self.kwargs.get("chapter_pk")
        queryset = FictionChapter.objects.filter(pk=chapter_pk)
        return queryset.get()

class FictionView(generic.DetailView):
    template_name = "fiction_fans/fiction_page.html"
    model = FictionTitle

    def get_object(self, queryse=None):
        return FictionTitle.objects.get(pk=self.kwargs.get("fiction_pk"))