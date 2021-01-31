import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import BadHeaderError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

import emails

from .models import Usuario
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users


@unauthenticated_user
def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user_email = form.cleaned_data.get("email")
            user_email = str(user_email)
            print(user_email)
            saved_password = form.cleaned_data.get("password1")
            saved_password = str(saved_password)
            print(saved_password)

            user.save()

            #Prepare email
            message = emails.html(
                html=f"<h4>Gracias por registrarse con nosotros</h4>"
                     f"<br><p>Contraseña: <strong>{saved_password}</strong></p>",
                subject="Enviado desde Challenge App",
                mail_from="julesc003@gmail.com"
            )
            try:
                # Send the email
                r = message.send(
                    to=user_email,
                    smtp={
                        "host": "email-smtp.us-east-1.amazonaws.com",
                        "port": 587,
                        "timeout": 5,
                        "user": "AKIAQWI6Q2LEBI5P3YWD",
                        "password": "5yRzEGE5aTb88peB2_YGe87wpm1rCkhD",
                        "tls": True,
                    },
                )
            except BadHeaderError:
                return HttpResponse(f"response: {r.status_code == 250}")

            return redirect("accounts:login-page")

    context = {
        "title": "Página de Registro",
        "form": form
    }

    return render(request, "accounts/register.html", context)


@unauthenticated_user
def login_page(request):
    """Log in a user"""
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if next in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("accounts:user-page")
    else:
        form = AuthenticationForm()

    context = {
        "title": "Página de Login",
        "form": form
    }

    return render(request, "accounts/login.html", context)


@login_required(login_url="accounts:login-page")
def user_page(request):
    usuario = Usuario.objects.all()

    context = {
        "title": "Página de Usuario",
        "usuario": usuario
    }

    return render(request, "accounts/user.html", context)


def logout_user(request):
    logout(request)
    return redirect("accounts:login-page")
