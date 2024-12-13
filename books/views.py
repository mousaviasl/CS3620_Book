from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book

def book_list(request):
    search_query = request.GET.get('q', '')
    books = Book.objects.filter(name__icontains=search_query)

    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'books/book_list.html', context)
