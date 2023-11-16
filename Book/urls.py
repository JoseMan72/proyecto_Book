from django.urls import path
from . import views

urlpatterns = [
   path('', views.BookListView, name='book_list'),
   path('detail/<int:pk>', views.BookDetailView, name='book_detail'),
   path('create/', views.BookCreateView, name='book_create'),
]