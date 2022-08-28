from django.db import models

# Create your models here.
class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    editedImg = models.ImageField(upload_to='images/')

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.editedImg.delete()
        super().delete(*args, **kwargs)