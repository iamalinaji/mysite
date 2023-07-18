from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy


class CustomPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset.html'
    email_template_name = 'account/password_reset_email.html'
    success_url = reverse_lazy('account:password_reset_done')


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('account:password_reset_complete')


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if '@' in username:
                user_to_be_authenticated = User.objects.filter(
                    email=username).first()
                if user_to_be_authenticated is not None:
                    username = user_to_be_authenticated.username

            user = authenticate(
                request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        return render(request, 'account/login.html')

    else:
        return redirect('/')


@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User created successfully')
                return redirect('account:login')
            else:
                messages.error(request, 'Account creation failed')
                return redirect('account:signup')
        else:
            return render(request, 'account/signup.html')
    else:
        return redirect('/')


def reset_password_request_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=form.cleaned_data['email'])
                # Generate a password reset token and create a password reset URL.
                token = default_token_generator.make_token(user)
                password_reset_url = reverse('password_reset_confirm',
                                             kwargs={'token': token})

                # Send the password reset email.
                send_mail(
                    'Password reset',
                    f'Click on this link to reset your password: {password_reset_url}',
                    'noreply@example.com',
                    [email],
                )

                return redirect('password_reset_sent')
            except:
                messages.error(request,
                               'There is no user with the associated email address')
                return redirect('account:reset_password_request')
    else:
        return render(request, 'account/resetpassword-request.html')
