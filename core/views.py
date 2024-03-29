from django.shortcuts import render, redirect
from .forms import SignupForm


def index(request):
    return render(request, 'core/index.html')


def contact(request):
    return render(request, 'core/contact.html')


def about(request):
    return render(request, 'core/about.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form,
    })
