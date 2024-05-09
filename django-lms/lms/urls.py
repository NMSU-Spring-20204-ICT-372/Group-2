from django.urls import path

from lms.views import index, add_book, add_genre, add_author, delete_book, delete_author, delete_genre

urlpatterns = [
    path('', index, name="lms-home"),
    path('add_book/', add_book, name="add_book"),
    path('add_author/', add_author, name="add_author"),
    path('add_genre/', add_genre, name="add_genre"),

    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    path('delete_author/<int:author_id>/', delete_author, name='delete_author'),
    path('delete_genre/<int:genre_id>/', delete_genre, name='delete_genre'),
]