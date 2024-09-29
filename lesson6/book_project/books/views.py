from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.http import HttpResponse


def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_add_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        published_date = request.POST.get('published_date')

        Book.objects.create(title=title, author=author, description=description, published_date=published_date)
        return redirect('book_list')

    return render(request, 'books/book_add.html')


def book_edit_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        book.published_date = request.POST.get('published_date')
        book.save()
        return redirect('book_list')

    return render(request, 'books/book_edit.html', {'book': book})


def book_delete_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'books/book_delete.html', {'book': book})
