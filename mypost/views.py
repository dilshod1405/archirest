from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import SignUpForm


def signup(request):
    if request.method == 'GET':
        user_form = SignUpForm()
        # print(user_form)
        # return HttpResponse(user_form.as_p())
        return render(request, template_name='signup.html', context={'form': user_form})
    else:
        user_register_form = SignUpForm(data=request.POST)
        if user_register_form.is_valid():
            user_register_form.save()
            user = user_register_form.instance
            return redirect('signin')
        else:
            return render(request, template_name='signup.html', context={'form': user_register_form})


def homepage(request):
    return render(request, template_name='base.html', context={'homepage':homepage})


def signin(request):
    return render(request, template_name='signin.html', context={'signin':signin})