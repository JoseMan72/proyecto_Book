from django.shortcuts import render
from django.views import View
from .models import Book

# Create your views here.
class BookListView(View):
   def get(self, request):
      books = Book.objects.all()
      return render(request, 'Book/listado.html', {'books': books})

class BookDetailView(View):
   def get(self, request, pk):
      book = Book.objects.get(id=pk)
      return render(request, 'Book/detalle.html', {'book': book})

#class BookCreateView(View):