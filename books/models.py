from django.db import models
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    info = models.TextField(max_length=10000, blank=True, null=True)
    pic = models.ImageField(upload_to='author/', null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    info = models.TextField(max_length=2000, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=22, default=0.00, help_text="UZS")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    pic = models.ImageField(upload_to="book/", null=True)

    def save(self, *args, **kwargs):
        if not self.author:
            self.author = "....."
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


