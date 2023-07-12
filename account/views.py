from django.shortcuts import render


def login_view(request):
    return render(request, 'account/login.html')


def logout_view(request):
    pass


def signup_view(request):
    return render(request, 'account/signup.html')
