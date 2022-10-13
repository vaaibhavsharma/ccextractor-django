from django.db import models


class Video(models.Model):
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.description