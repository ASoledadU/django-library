from django.contrib import admin
from django.urls import path
import app.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", app.views.home, name="home"),
    path("book/<id>/borrow", app.views.borrow_book, name="borrow_book"),
    path("book/<id>/return", app.views.return_book, name="return_book")
    ]
