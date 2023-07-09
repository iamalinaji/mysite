from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import ContactForm
from django.shortcuts import redirect
from django.contrib import messages


def home_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = 'Unknown'
            contact = form.save(commit=False)
            contact.name = name
            contact.save()
            messages.success(request, "Your ticket was submitted successfully")
            return redirect('/contact')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Your ticket was not submitted")
    return render(request, 'website/contact.html')
