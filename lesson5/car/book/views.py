from django.shortcuts import render

from .form import BookForm


# Create your views here.


def book_info_view(request, *args, **kwargs ):
    if request.method == 'POST':
        pass
    else:
        form = BookForm()
        context = {'form': form}
        return render(request, 'books.html', context)
