"""Create view for reading fiction's story."""
from django.shortcuts import render
from ..models import FictionTitle, FictionChapter
from django.views import generic

# Create your views here.


class ChapterView(generic.DetailView):
    """Create view for reading fiction's chapter page."""
    template_name = "fiction_fans/chapter_page.html"
    model = FictionChapter

    def get_object(self, queryset=None):
        """ 
        Get chapter object from query and return it to render method.
        """
        chapter_pk = self.kwargs.get("chapter_pk")
        queryset = FictionChapter.objects.filter(pk=chapter_pk)
        return queryset.get()

class FictionView(generic.DetailView):
    """Create view for viewing detail of fiction
    
        this page will display:
        1. Synopsis
        2. Fiction title
        3. list of chapters
        4. fiction genre
        5. fiction cover
    """
    template_name = "fiction_fans/fiction_page.html"
    model = FictionTitle

    def get_object(self, queryse=None):
        return FictionTitle.objects.get(pk=self.kwargs.get("fiction_pk"))