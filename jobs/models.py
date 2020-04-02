from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.title
