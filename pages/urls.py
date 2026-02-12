from django.urls import path
from .views import HompePageView, AboutPageView


urlpatterns = [
    path("", HompePageView.as_view(), name="home"),
    path("home/", HompePageView.as_view(), name="homeTwo"),
    path("about/", AboutPageView.as_view(), name="about"),
]

