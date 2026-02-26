from django.shortcuts import render
from django.views.generic import(
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView
)
from .models import Post, Status
from django.urls import reverse_lazy


# Create your views here.
class PostListView(ListView):
    template_name = "posts/list.html"
    #model = Post
    published_status = Status.objects.get(Name="published")
    # queryset attribute allows us to select some data from the db by using the model class
    queryset = Post.objects.filter(status=published_status).order_by("created_on")
    context_object_name = "posts"
    # this mehod helps us to use the context howeverr we want ( take a look at it, add elements or anything)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "post"

class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")