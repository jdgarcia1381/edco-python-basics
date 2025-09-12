from django.urls import path

from . import views

app_name = "libros"
urlpatterns = [
    path("", views.index, name="home"),
    path("lista/", views.lista_libros, name="lista_libros"),
]
