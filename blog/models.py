from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def pretty_pub_date(self):
        return self.pub_date.strftime('%b %e %Y')

    def limited_body(self):
        return " ".join(self.body.split()[:140])
