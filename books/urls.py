from django.urls import path
from .views import home, register, login_view, logout_view, book_list, add_book, edit_book, delete_book


urlpatterns = [
    path("", home, name="home"),  # Default landing page
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("books/", book_list, name="book_list"),
    path("add/", add_book, name="add_book"),
    path("edit/<int:book_id>/", edit_book, name="edit_book"),
    path("delete/<int:book_id>/", delete_book, name="delete_book"),
]