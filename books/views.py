from django.shortcuts import render, redirect
from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()

    context = {
        'books':books
    }

    return render(request, 'books/index.html',context)

def new(request):
    return render(request, 'books/new.html')

def create(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    review_num = request.POST.get('review_num')
    author = request.POST.get('author')

    book = Book(
        title=title,
        description=description,
        review_num=review_num,
        author=author
    )
    book.save()

    return redirect('books:detail', book.pk)

def detail(request, pk):
    book = Book.objects.get(pk=pk)
    
    context = {
        'book':book,
    }

    return render(request, 'books/detail.html', context)

def update(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
    }
    return render(request, 'books/update.html', context)

def edit(request,pk):
    book = Book.objects.get(pk=pk)

    title = request.POST.get('title')
    description = request.POST.get('description')
    review_num = request.POST.get('review_num')
    author = request.POST.get('author')

    book.title = title
    book.description = description
    book.review_num = review_num
    book.author = author

    book.save()

    return redirect('books:detail', book.pk)

def delete(request,pk):
    book = Book.objects.get(pk=pk)

    book.delete()

    return redirect('books:index')