from django.db import models
import authors
from django.shortcuts import reverse
from authors.models import Author

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=100)
    pages = models.IntegerField()

    author = models.ForeignKey    (
        Author,
        on_delete=models.CASCADE,
        related_name="books",
        null=True,
        blank=True
    )
    price = models.IntegerField()

    cover = models.ImageField(upload_to='books/images/', blank=True, null=True)
    def __str__(self):
        return self.name

    @property
    def image_url (self):
        return f'/media/{self.cover}'
    @property
    def show_url (self):
        url = reverse('bookdetail', args=[self.id])
        return url

    @property
    def edit_url(self):
        url = reverse("editbook", args=[self.id])
        return url
