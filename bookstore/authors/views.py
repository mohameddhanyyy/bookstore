from django.shortcuts import render
from authors.models import Author

def authors(request):
    authors = Author.objects.all()
    return render(request, "authors/authors.html", {"authors": authors})
