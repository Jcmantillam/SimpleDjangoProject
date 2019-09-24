from django.http import HttpResponse
from django.shortcuts import render,redirect


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