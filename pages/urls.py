from django.urls import path
from .views import HomePageView, AboutPageView, PagesPageView

urlpatterns = [
    path("pages/", PagesPageView.as_view(), name='pages'),
    path("about/", AboutPageView.as_view(), name="about"),
    path('',HomePageView.as_view(), name='home'),
]