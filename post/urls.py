from django.urls import path
from .views import(
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostdraftView,
    PostarchiveView

) 


urlpatterns = [
    path("list/", PostListView.as_view(), name="post_list"),
    path("new/", PostCreateView.as_view(), name="post_new"),
    path("draft/", PostdraftView.as_view(), name="post_draft"),
    path("archive/", PostarchiveView.as_view(), name="post_archive"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("<int:pk>/delete", PostDeleteView.as_view(), name="post_delete")
]