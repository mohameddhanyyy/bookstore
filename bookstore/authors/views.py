# # authors/views.py
# from django.shortcuts import get_object_or_404, redirect, render
# from authors.forms import AuthorForm
# from authors.models import Author


# def authors(request):
#     authors = Author.objects.prefetch_related("books").all()
#     return render(request, "authors/authors.html", {"authors": authors})


# def createauthor(request):
#     if request.method == "POST":
#         form = AuthorForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("authors:authors")
#     else:
#         form = AuthorForm()
#     return render(request, "authors/createauthor.html", {"form": form})


# def editauthor(request, id):
#     author = get_object_or_404(Author, id=id)
#     if request.method == "POST":
#         form = AuthorForm(request.POST, request.FILES, instance=author)
#         if form.is_valid():
#             form.save()
#             return redirect("authors:authors")
#     else:
#         form = AuthorForm(instance=author)
#     return render(request, "authors/editauthor.html", {"form": form, "author": author})

# def deleteauthor(request, id):
#     author = get_object_or_404(Author, id=id)
#     author.delete()
#     return redirect("authors:authors")




from django.urls import reverse_lazy
from authors.forms import AuthorForm
from authors.models import Author
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


class AuthorListView(ListView):
    model = Author
    template_name = "authors/authors.html"
    context_object_name = "authors"


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "authors/createauthor.html"
    success_url = "/authors/"


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = "authors/editauthor.html"
    success_url = "/authors/"


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = "authors/deleteauthor.html"
    success_url = reverse_lazy("authors:authors")


