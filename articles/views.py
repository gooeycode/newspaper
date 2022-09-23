from django.shortcuts import render

#import list and detail views from django
from django.views.generic import ListView, DetailView, CreateView

#import views that allow for editing and deleting
from django.views.generic.edit import UpdateView, DeleteView # new

#import articles objects to create list view
from .models import Article

#import reverse lazy to convert view name into url
from django.urls import reverse_lazy

#create view that lists article using template
class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleUpdateView(UpdateView): 
    model = Article
    fields = (
    "title",
    "body",
    )
    template_name = "article_edit.html"

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        "author",
    )
