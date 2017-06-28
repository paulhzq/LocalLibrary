from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,'num_visits':num_visits},
    )
class BookListView(generic.ListView):
    model = Book
    # context_object_name = 'my_book_list'   # your own name for the list as a template variable
    # # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # queryset = Book.objects.all()
    # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author


from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


from django.contrib.auth.mixins import PermissionRequiredMixin

class LoanedBooksAllListView(PermissionRequiredMixin,generic.ListView):
    """
    List all the borrowed books(only viewed by libraian).
    """
    permission_required = ('catalog.can_mark_returned')
    model = BookInstance
    template_name = 'catalog/bookintance_list_borrowed_all.html'

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')
