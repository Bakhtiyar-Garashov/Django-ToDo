from django.db import models


# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
