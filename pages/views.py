from django.views.generic import TemplateView

# Create your views here.

class HompePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"
