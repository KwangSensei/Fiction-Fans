"""Create the fiction and add mutiple chapter to fiction."""
from django.db import models
from django.conf import settings
from django_editorjs import EditorJsField

# Create your models here.
    

class FictionTitle(models.Model):
    """Create fiction that contain fiction's title and created date/time."""
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255,)
    status = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class FictionChapter(models.Model):
    """
    Create a chapter for fiction that contain chapter's title
    and chapter's content.
    Connect each chapter to a single fiction by using ForeignKey.
    """
    title = models.CharField(max_length=255)
    content = EditorJsField(
        editorjs_config={
            "tools": {
                "Image": {
                    "config": {
                        "endpoints": {
                            "byFile": "/fiction/imageUPload/",
                            "byUrl": "/fiction/imageUPload/",
                        },
                        "additionalRequestHeaders": [{"Counter-Type": 'multipart/form-data'}]
                    }
                }
            }
        }
    )
    fiction_title = models.ForeignKey(FictionTitle, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.fiction_title}: {self.title}"
