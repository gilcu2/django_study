from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),

    path('books/', book_list, name='book_list_fbv'),
    path('books/<int:book_id>/', book_detail, name='book_detail_fbv'),
    path('authors//books/', books_by_author,name='books_by_author'),

    path('cbv/books/', BookListView.as_view(), name='book_list_cbv'),
    path('cbv/books//', BookDetailView.as_view(),
         name='book_detail_cbv'),
]
