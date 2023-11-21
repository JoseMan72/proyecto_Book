from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookEditView, BookDeleteView

urlpatterns = [
   path('', BookListView.as_view(), name='book_list'),
   path('details/<int:pk>', BookDetailView.as_view(), name='book_details'),
   path('create/', BookCreateView.as_view(), name='book_create'),
   path('edit/<int:pk>', BookEditView.as_view(), name='book_edit'),
   path('delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
]