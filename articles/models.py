from django.db import models

from django.conf import settings #so we can use the custom user model

from django.urls import reverse #so we can reverse search the url


#creating class for articles, inherits from the modern class
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #referencing our custom model (AUTH_USER_MODEL) author from settings.py
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

#return the title of the instantiated object
    def __str__(self):
        return self.title

#get url of this object using the primary key of this object
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk":self.pk})