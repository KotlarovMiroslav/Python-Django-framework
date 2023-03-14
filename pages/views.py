from django.shortcuts import render
# Create your views here.
# from django.http import HttpResponse

# def homePageView(request):
#     return HttpResponse('Hello, World!')

from django.views.generic import TemplateView, ListView
from .models import Post

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = "about.html"

class PagesPageView(ListView):
    model = Post
    template_name = "pages.html"