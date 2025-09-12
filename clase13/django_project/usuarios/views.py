from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import RegistroUsuarioForm
from .models import Usuario


# Create your views here.
def crear_usuario(request):
    # Opción 1
    usuario = Usuario.objects.create(nombre="Ana García", correo="ana@email.com")
    # Opción 2
    usuario = Usuario(nombre="Carlos López", correo="carlos@email.com")
    usuario.save()


def listar_usuarios_queries(request):
    usuarios = Usuario.objects.all()
    usuarios = Usuario.objects.exclude(nombre="Ana")
    usuarios = Usuario.objects.filter(Q(nombre="Ana") | Q(nombre="Pedro"))
    usuarios = Usuario.objects.filter(edad__gte=18)
    usuarios = Usuario.objects.filter(id__in=[1, 2, 3])
    usuario = Usuario.objects.get(id=1)


def actualizar_usuario(request):
    usuario = Usuario.objects.get(id=1)
    usuario.correo = "nuevo@email.com"
    usuario.save()
    # UPDATE USUARIOS SET correo="nuevo@email.com" WHERE id=1;

    Usuario.objects.filter(fecha_registro__year=2023).update(activo=True)


def eliminar_usuario(request):
    usuario = Usuario.objects.get(id=1)
    usuario.delete()
    # DELETE FROM USUARIOS WHERE ID = 1;
    Usuario.objects.filter(activo=False).delete()
    Usuario.objects.all().delete()


def inicio(request):
    mensaje = "¡Bienvenido a la Biblioteca Virtual!"
    return HttpResponse(f"<h1>{mensaje}</h1><p>Tu portal de conocimiento digital</p>")


def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "usuarios/lista.html", {"usuarios": usuarios})


def registrar_usuario_base(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            correo = form.cleaned_data["correo"]
            edad = form.cleaned_data["edad"]
            # Procesar los datos (guardar en BD, enviar email, etc.)
            # Usuario.objects.create(nombre=nombre, correo=correo, edad=edad)
            return redirect("confirmacion")
        else:  # If the form is not valid, re-render with errors
            pass  # The form object 'form' already contains errors
    else:  # If request method is GET, display a new, empty form
        form = RegistroUsuarioForm()
    return render(request, "registro.html", {"form": form})


def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, "Usuario registrado exitosamente!")
            return redirect("usuarios:confirmacion_usuario", usuario_id=usuario.id)
    else:
        form = RegistroUsuarioForm()

    return render(request, "usuarios/registrar_usuario.html", {"form": form})


def confirmacion_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    return render(request, "usuarios/confirmacion.html", {"usuario": usuario})
