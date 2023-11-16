from django.shortcuts import render, redirect
from django.views import View
from .models import Book
from .forms import BookForm

# Create your views here.
class BookListView(View):
   def get(self, request):
      books = Book.objects.all()
      return render(request, 'Book/list.html', {'books': books})

class BookDetailView(View):
   def get(self, request, pk):
      book = Book.objects.get(id=pk)
      return render(request, 'Book/details.html', {'book': book})

class BookCreateView(View):
   def get(self, request):
      form = BookForm()
      return render(request, 'Book/create.html', {'form': form})
   
   def post(self, request):
      form = BookForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('book_list')
      return render(request, 'Book/create.html', {'form': form})

class BookEditView(View):
   def get(self, request, pk):
      book = Book.objects.get(id=pk)
      form = BookForm(instance=book)
      return render(request, 'Book/edit.html', {'form': form, 'book': book})
   
   def post(self, request, pk):
      book = Book.objects.get(id=pk)
      form = BookForm(request.POST, instance=book)
      if form.is_valid():
         form.save()
         return redirect('book_list')
      return render(request, 'Book/edit.html', {'form': form, 'book': book})