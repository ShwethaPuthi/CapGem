from django.shortcuts import render
from django.urls import reverse_lazy #used to take care of no reverse match error
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Book
# Create your views here.
class BookListView(ListView):
    model = Book
    template_name='book_list.html'
