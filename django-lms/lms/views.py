from django.shortcuts import get_object_or_404, redirect, render
from .models import Book, Author, Genre


def index(request):
    registered_books = Book.objects.all()
    context = {
        'books': registered_books
    }
    return render(request, 'lms/index.html', context)


def add_author(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        author = Author.objects.create(name=name)
        
        return redirect('add_author')
    else:
        return render(request, 'lms/add_author.html')


def add_genre(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        genre = Genre.objects.create(name=name)
        
        return redirect('add_genre')
    else:
        return render(request, 'lms/add_genre.html')


def add_book(request):
    if request.method == 'POST':
        # Extract data from the form
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        genre_id = request.POST.get('genre')
        description = request.POST.get('description')
        published_date = request.POST.get('published_date')
        isbn = request.POST.get('isbn')

        author = Author.objects.get(id=author_id)
        genre = Genre.objects.get(id=genre_id)

        book = Book.objects.create(
            title=title,
            author=author,
            genre=genre,
            description=description,
            published_date=published_date,
            isbn=isbn
        )

        return redirect('lms-home')
    else:
        return render(request, 'lms/add_book.html', {'books': Book.objects.all(), 'authors': Author.objects.all(), 'genres': Genre.objects.all()})
    

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('lms-home')  # Replace 'home' with the name of your home view
    return redirect('lms-home')  # Redirect to home page if the request method is not POST