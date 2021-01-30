from django.shortcuts import render


def register_page(request):
    context = {
        "title": "Página de Registro"
    }

    return render(request, "accounts/register.html", context)


def login_page(request):
    context = {
        "title": "Página de Login"
    }

    return render(request, "accounts/login.html", context)


def user_page(request):
    context = {
        "title": "Página de Usuario"
    }

    return render(request, "accounts/user.html", context)


def logout_user(request):
    pass
