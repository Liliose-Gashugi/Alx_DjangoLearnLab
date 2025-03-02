from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('login')  # Change 'home' to your actual home page
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Adjust the redirect
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

# Test functions for each role
def admin_required(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def librarian_required(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def member_required(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views

@user_passes_test(admin_required)
def admin_view(request):
    return HttpResponse("Hello, Admin! This view is restricted to Admin users.")

@user_passes_test(librarian_required)
def librarian_view(request):
    return HttpResponse("Hello, Librarian! This view is restricted to Librarian users.")

@user_passes_test(member_required)
def member_view(request):
    return HttpResponse("Hello, Member! This view is restricted to Member users.")
