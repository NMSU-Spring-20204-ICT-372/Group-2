from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book

# Create your views here
def index(request):
    registered_books = Book.objects.all()
    context = {
        'books': registered_books
    }
    return render(request, 'lms/index.html', context)