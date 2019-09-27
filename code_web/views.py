from django.http import HttpResponse
from io import BytesIO
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

from code_web.models import *

def home(request):
    return render(
        request,
        "home.html"
    )

def about(request):
    return render(
        request,
        "about.html"
    )

def root(request):
    return redirect("/home")

def form(request):
    print("form")
    if request.method == "POST":
        print("post")
        #Recolectar la info del formulario
        _nombre = request.POST.get("nombre")
        _email = request.POST.get("email")
        _comentarios = request.POST.get("comentarios")
        
        usuario = usuarios_registrados.objects.create(nombre=_nombre)
        usuario.email = _email
        usuario.comentarios = _comentarios
        usuario.save()
        
        enviar_mail(_nombre, _email)
        
        return render(
            request,
            "Form_mail.html"
        )
    else:
        print("Get")
        return render(
        request,
        "Form_mail.html"
    )
    
def enviar_mail(name, email):

    email = EmailMessage('PWA Demo', 'Gracias por tus cometarios', to=[email])
    email.send()