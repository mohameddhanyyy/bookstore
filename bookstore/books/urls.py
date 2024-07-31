# from django.urls import include, path
# from django.conf.urls.static import static
# from authors.views import authors

# from bookstore import settings
# from . import views

# from django.urls import path
# from books.views import BookListView, BookCreateView, BookUpdateView, BookDeleteView

# urlpatterns = [
#     path("home/", views.home, name="home"),
#     path("contactus/", views.contactus, name="contactus"),
#     path("authors/", include("authors.urls", namespace="authors")),
#     path("aboutus/", views.aboutus, name="aboutus"),
#     path("<int:id>/bookdetail", views.bookdetail, name="bookdetail"),
#     path("<int:id>/bookdelete", views.bookdelete, name="bookdelete"),
#     path("createbook/", views.createbook, name="createbook"),
#     path("<int:id>/editbook", views.edit, name="editbook"),
#     # path("authors/", views.authors, name="authors"),
# ]
# from django.urls import path

# from authors import views
# from .views import (
#     BookListView,
#     BookDetailView,
#     BookCreateView,
#     BookUpdateView,
#     BookDeleteView,
# )

# urlpatterns = [
#     # other URL patterns
#     path("", BookListView.as_view(), name="home"),
#     path("book/<int:pk>/", BookDetailView.as_view(), name="bookdetail"),
#     path("book/create/", BookCreateView.as_view(), name="createbook"),
#     path("book/<int:pk>/edit/", BookUpdateView.as_view(), name="editbook"),
#     path("book/<int:pk>/delete/", BookDeleteView.as_view(), name="deletebook"),

# ]
# books/urls.py

from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

app_name = "books"

urlpatterns = [
    path("", BookListView.as_view(), name="home"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="bookdetail"),
    path("book/create/", BookCreateView.as_view(), name="createbook"),
    path("book/<int:pk>/edit/", BookUpdateView.as_view(), name="editbook"),
    path("book/<int:pk>/delete/", BookDeleteView.as_view(), name="deletebook"),
]
