from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title