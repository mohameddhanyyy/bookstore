# from django.urls import path
# from django.conf.urls.static import static

# from bookstore import settings
# from . import views

# app_name = 'authors'

# # urlpatterns = [
# #     path("", views.authors, name="authors"),
# #     path("createauthor", views.createauthor, name="createauthor"),
# # ]


# urlpatterns = [
#     path("", views.authors, name="authors"),
#     path("create/", views.createauthor, name="createauthor"),
#     path("<int:id>/edit/", views.editauthor, name="editauthor"),
#     path("<int:id>/delete/", views.deleteauthor, name="deleteauthor"),
# ]


from django.urls import path
from authors.views import (
    AuthorListView,
    AuthorCreateView,
    AuthorUpdateView,
    AuthorDeleteView,
)

app_name = "authors"

urlpatterns = [
    path("", AuthorListView.as_view(), name="authors"),
    path("create/", AuthorCreateView.as_view(), name="createauthor"),
    path("edit/<int:pk>/", AuthorUpdateView.as_view(), name="editauthor"),
    path("delete/<int:pk>/", AuthorDeleteView.as_view(), name="deleteauthor"),
    
]
