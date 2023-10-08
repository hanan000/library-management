from typing import Any

from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm


def index(request):
    """View function for the index page.

    Displays a list of books categorized into 'Art' and 'Technology' shelves.
    Allows users to add new books using a form.

    Parameters:
        request: The HTTP request object.

    Returns:
        The HTTP response containing the rendered index.html template.
    """

    books_art = Book.objects.filter(shelf='Art')
    books_technology = Book.objects.filter(shelf='Technology')

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()

    all_books = Book.objects.all()

    return render(request, 'index.html',
                  {'form': form, 'books_art': books_art, 'books_technology': books_technology, 'all_books': all_books})


def edit_book(request: Any, book_id: int):
    """View function for editing a book's details.
    Allows users to update a book's title, author, and published date.

    Parameters:
        request: The HTTP request object.
        book_id: The ID of the book to be edited.

    Returns:
        The HTTP response containing the rendered edit_book.html template.
    """
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        # Update the book attributes with the new values if provided
        book.title = request.POST.get('new_title', book.title)
        book.author = request.POST.get('new_author', book.author)
        book.published_date = request.POST.get('new_date', book.published_date)

        book.save()

        return redirect('index')

    return render(request, 'edit_book.html', {'book': book})


def delete_book(request: Any, book_id: int):
    """View function for deleting a book.
    Allows users to delete a book from the database.

    Parameters:
        request: The HTTP request object.
        book_id: The ID of the book to be deleted.

    Returns:
        HttpResponse: Redirects to the index page after deleting the book.
    """
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        book.delete()

    return redirect('index')
