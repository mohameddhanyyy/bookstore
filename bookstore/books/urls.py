from django.urls import path
from django.conf.urls.static import static
from authors.views import authors

from bookstore import settings
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("contactus/", views.contactus, name="contactus"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("<int:id>/bookdetail", views.bookdetail, name="bookdetail"),
    path("<int:id>/bookdelete", views.bookdelete, name="bookdelete"),
    path("createbook/", views.createbook, name="createbook"),
    path("<int:id>/editbook", views.edit, name="editbook"),
    # path("authors/", views.authors, name="authors"),
]
