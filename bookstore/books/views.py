# from django.shortcuts import render, get_object_or_404, redirect

# from authors.models import Author
# from .models import Book


# def home(request):
#     booklist = Book.objects.all()
#     return render(request, "books/home.html", {"booklist": booklist})


# def contactus(request):
#     return render(request, "books/contactus.html")


# def aboutus(request):
#     return render(request, "books/aboutus.html")


# def bookdetail(request, id):
#     book = get_object_or_404(Book, id=id)
#     return render(request, "books/bookdetail.html", {"book": book})


# def bookdelete(request, id):
#     book = get_object_or_404(Book, id=id)
#     book.delete()
#     return redirect("home")


# def createbook(request):
#     if request.method == "POST":

#         name = request.POST.get("name")
#         no_pages = request.POST.get("pages")
#         price = request.POST.get("price")
#         cover = request.FILES.get("cover")
#         author_id = request.POST.get("author")


#         author = Author.objects.get(id=author_id)

#         book = Book.objects.create(
#             name=name, no_pages=no_pages, cover= cover, price=price, author=author
#         )
#         return redirect(book.show_url)
#     else:
#         authors = Author.objects.all()
#         context = {'authors': authors}
#         return render(request, "books/createbook.html", context)


# def edit (request, id):
#     book = get_object_or_404(Book, id=id)
#     if request.method == "POST":
#         book.name = request.POST.get("name")
#         book.author = request.POST.get("author")
#         book.no_pages = request.POST.get("pages")
#         book.price = request.POST.get("price")
#         book.cover = request.FILES.get("cover")
#         book.save()
#         return redirect(book.show_url)
#     return render(request, "books/editbook.html", {"book": book})


from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Book
from authors.models import Author
from .forms import BookForm


class BookListView(ListView):
    model = Book
    template_name = "books/home.html"
    context_object_name = "booklist"


class BookDetailView(DetailView):
    model = Book
    template_name = "books/bookdetail.html"
    context_object_name = "book"


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "books/createbook.html"
    success_url = reverse_lazy(
        "books:home"
    )  # Redirect to the book list after successful creation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = Author.objects.all()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/editbook.html"
    success_url = reverse_lazy("books:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = Author.objects.all()
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["author"].queryset = Author.objects.all()
        return form


class BookDeleteView(DeleteView):
    model = Book
    template_name = "books/deletebook.html"
    success_url = reverse_lazy("books:home")
