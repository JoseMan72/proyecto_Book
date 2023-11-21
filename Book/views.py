from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm

# Create your views here.
'''
class BookListView(View):
   def get(self, request):
      books = Book.objects.all()
      return render(request, 'Book/list.html', {'books': books})

class BookDetailView(View):
   def get(self, request, pk):
      book = Book.objects.get(id=pk)
      return render(request, 'Book/details.html', {'book': book})

class BookCreateView(CreateView):
   model = Book

class BookEditView(View):
   def get(self, request, pk):
      book = Book.objects.get(id=pk)
      form = BookForm(instance=book)
      return render(request, 'Book/book_edit.html', {'form': form, 'book': book})
   
   def post(self, request, pk):
      book = Book.objects.get(id=pk)
      form = BookForm(request.POST, instance=book)
      if form.is_valid():
         form.save()
         return redirect('book_list')
      return render(request, 'Book/book_edit.html', {'form': form, 'book': book})
'''

class BookListView(ListView):
   model = Book

class BookCreateView(View):
   def get(self, request):
      return render(request, 'Book/book_create.html',
                     context={'forms': formset_factory(BookForm, extra=2)})
   
   def post(self, request):
      formset = formset_factory(BookForm)
      formset = formset(data=request.POST)

      if formset.is_valid():
         for form in formset:
            if form.has_changed():
               form.save()
         return redirect(to='book_list')
      
      else:
         return render(request, 'Book/book_create.html', 
                        context={'forms': formset})

class BookDetailView(DetailView):
   model = Book

class BookEditView(UpdateView):
   model = Book
   fields = ['title', 'author', 'rating', 'sinopsis']
   template_name_suffix = "_edit"
   success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
   model = Book
   success_url = reverse_lazy('book_list')