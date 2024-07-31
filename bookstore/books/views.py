from django.shortcuts import render, get_object_or_404, redirect

from authors.models import Author
from .models import Book


def home(request):
    booklist = Book.objects.all()
    return render(request, "books/home.html", {"booklist": booklist})


def contactus(request):
    return render(request, "books/contactus.html")


def aboutus(request):
    return render(request, "books/aboutus.html")


def bookdetail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "books/bookdetail.html", {"book": book})


def bookdelete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect("home")


def createbook(request):
    if request.method == "POST":
        # Get form data
        name = request.POST.get("name")
        no_pages = request.POST.get("pages")
        price = request.POST.get("price")
        cover = request.FILES.get("cover")
        author_id = request.POST.get("author")

        # Get the author object
        author = Author.objects.get(id=author_id)

        # Create new book
        book = Book.objects.create(
            name=name, no_pages=no_pages, cover= cover, price=price, author=author
        )
        return redirect(book.show_url)
    else:
        authors = Author.objects.all()
        context = {'authors': authors}
        return render(request, "books/createbook.html", context)


def edit (request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.name = request.POST.get("name")
        book.author = request.POST.get("author")
        book.no_pages = request.POST.get("pages")
        book.price = request.POST.get("price")
        book.cover = request.FILES.get("cover")
        book.save()
        return redirect(book.show_url)
    return render(request, "books/editbook.html", {"book": book})
