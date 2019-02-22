from django.shortcuts import *
from library.forms import *


# Create your views here.
def index(request):
    books = Book.objects.all()
    authors = Author.objects.filter(active=True)
    return render(request, 'index.html', {'books': books,
                                          'authors': authors})


def show_authors(request):
    authors = Author.objects.all()
    return render(request, 'show_authors.html', {'authors': authors})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)

        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            form.save()
            return redirect('author_details', pk=author.pk)
    else:
        form = AuthorForm()

        return render(request, 'add_author.html', {'form': form})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            form.save_m2m()
            return redirect('book_details', pk=book.pk)
    else:
        form = BookForm()

        return render(request, 'add_book.html', {'form': form})


def author_details(request, pk):
    author = Author.objects.get(id=pk)
    all_books = Book.objects.all()
    books = list()

    for book in all_books:
        if author in book.authors.all():
            books.append(book)

    return render(request, 'author_details.html', {'author': author,
                                                   'books': books})


def book_details(request, pk):
    book = Book.objects.get(id=pk)

    return render(request, 'book_details.html', {'book': book})


def inactivate_or_activate_author(request, pk):
    author = Author.objects.get(id=pk)
    if author.active:
        author.active = False
    else:
        author.active = True
    author.save()
    return redirect('author_details', pk=author.pk)
