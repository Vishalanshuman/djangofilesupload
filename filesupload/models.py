from django.db import models

# Create your models here.

class PhotoAlbum(models.Model):
    name = models.CharField(max_length=200)
    images = models.FileField(upload_to= 'File_album')

    def __str__(self) -> str:
        return self.name