from django.urls import path

from lms.views import add_customer, delete_customer, index, checked_out_book, add_book, add_genre, add_author, delete_book, delete_author, delete_genre, delete_checked_out

urlpatterns = [
    path('', index, name="lms-home"),
    path('add_customer/', add_customer, name="add_customer"),
    path('add_book/', add_book, name="add_book"),
    path('add_author/', add_author, name="add_author"),
    path('add_genre/', add_genre, name="add_genre"),

    path('checked_out_book/', checked_out_book, name="checked_out_book"),

    path('delete_customer/<int:customer_id>/', delete_customer, name='delete_customer'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    path('delete_author/<int:author_id>/', delete_author, name='delete_author'),
    path('delete_genre/<int:genre_id>/', delete_genre, name='delete_genre'),

    path('delete_checked_out/<int:checked_out_id>/', delete_checked_out, name='delete_checked_out'),
]