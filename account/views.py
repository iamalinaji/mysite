from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(
                    request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        return render(request, 'account/login.html')

    else:
        return redirect('/')


def logout_view(request):
    pass


def signup_view(request):
    return render(request, 'account/signup.html')
