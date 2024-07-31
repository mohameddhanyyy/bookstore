# authors/models.py
from audioop import reverse
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100 , null=True, blank=True)
    image = models.ImageField(upload_to="authors/images/", null=True, blank=True)
    bdate = models.DateField( null=True, blank=True, default="1990-01-01")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True , null=True)

    def __str__(self):
        return self.name

    @property
    def show_url(self):
        url = reverse("authors", args=[self.id])
        return url
