from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from .forms import CreateUserForm


def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            saved_password = form.cleaned_data.get("password1")
            print(saved_password)

            user.save()

            return redirect("accounts:login-page")

    context = {
        "title": "Página de Registro",
        "form": form
    }

    return render(request, "accounts/register.html", context)


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


def user_page(request):
    context = {
        "title": "Página de Usuario"
    }

    return render(request, "accounts/user.html", context)


def logout_user(request):
    logout(request)
    return redirect("accounts:login-page")
