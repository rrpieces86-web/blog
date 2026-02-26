from django.shortcuts import render
from django.views.generic import(
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView
)
from .models import Post
from django.urls import reverse_lazy


# Create your views here.
class PostListView(ListView):
    template_name = "post/list.html"
    model = Post
    context_object_name = "posts"

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
