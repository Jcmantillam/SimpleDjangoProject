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
        post = True
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
            "Form_mail.html",
            {
                "post" : post,
            }
        )
    else:
        print("Get")
        return render(
        request,
        "Form_mail.html"
    )
    
def enviar_mail(name, email):

    content = render_to_string("email_content.html")
    #print(content)
    email = EmailMessage('PWA Demo', content, to=[email])
    email.content_subtype = 'html'
    email.send()
    
def galeria(request):
    return render(
        request,
        "galeria.html"
    )
    
def coms(request):
    comentarios = usuarios_registrados.objects.values("nombre","email","comentarios")
    lista_comentarios = []
    for c in comentarios:
        nombre = c["nombre"]
        mail = c["email"]
        comentario = c["comentarios"]
        print(nombre)
        values = []
        values.append(nombre)
        values.append(mail)
        values.append(comentario)
        lista_comentarios.append(values)
    print(lista_comentarios)
    return render(
        request,
        "comentarios.html",
        {
            "lista_comentarios": lista_comentarios,
        }
    )