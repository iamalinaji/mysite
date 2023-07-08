from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages


def home_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your message has been sent successfully.')
            return redirect('/contact')
        else:
            messages.error(
                request, 'There was an error saving your message')
    return render(request, 'contact.html', {'form': form})
