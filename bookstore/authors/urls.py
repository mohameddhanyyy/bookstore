from django.urls import path
from django.conf.urls.static import static

from bookstore import settings
from . import views

app_name = 'authors'

urlpatterns = [
    path("", views.authors, name="authors"),
]
