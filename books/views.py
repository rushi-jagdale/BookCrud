from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book

# Check if the user is an admin
def is_admin(user):
    return user.is_superuser

def home(request):
    return render(request, "home.html")

# User Registration
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect("book_list")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

# User Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("book_list")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

# User Logout
def logout_view(request):
    logout(request)
    return redirect("login")

# List Books (Login Required)
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})

# Add Book (Admin Only)
@user_passes_test(is_admin)
def add_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        published_date = request.POST["published_date"]
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect("book_list")
    return render(request, "add_book.html")

# Edit Book (Admin Only)
@user_passes_test(is_admin)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST["title"]
        book.author = request.POST["author"]
        book.published_date = request.POST["published_date"]
        book.save()
        return redirect("book_list")
    return render(request, "edit_book.html", {"book": book})

# Delete Book (Admin Only)
@user_passes_test(is_admin)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect("book_list")
