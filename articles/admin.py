from django.contrib import admin

#import the articles model
from .models import Article

#add article classes & objects to admin view
admin.site.register(Article)
# Register your models here.
