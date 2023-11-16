from django.urls import path
from . import views

urlpatterns = [
   path('', views.BookListView.as_view(), name='book_list'),
   path('details/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
   path('create/', views.BookCreateView.as_view(), name='book_create'),
   path('edit/<int:pk>', views.BookEditView.as_view(), name='book_edit'),
]