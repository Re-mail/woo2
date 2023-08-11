from django.shortcuts import render, redirect
from django.db import transaction
from .models import User
from argon2 import PasswordHasher
from .forms import RegisterForm

# Create your views here.
def register(request):
    register_form = RegisterForm()
    context = {'forms' : register_form}

    if request.method == 'GET':
        return render(request, 'user/register.html', context)
    
    elif request.method =='POST':
        # user_email = request.POST.get('email','')
        # user_name = request.POST.get('name','')
        # user_pw = request.POST.get('pw','')
        # user_pw_confirm = request.POST.get('pw-confirm','')

        # if (user_email or user_name or user_pw or user_pw_confirm) == '':
        #     return redirect('/user/register')
        # elif user_pw !=user_pw_confirm:
        #     return redirect('user/register')
        # else:
        #     user=User(
        #         user_email = user_email,
        #         user_name = user_name,
        #         user_pw = user_pw
        #     )
        #     user.save()
        # return redirect('/')
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user=User(
                user_email = register_form.user_email,
                user_name = register_form.user_name,
                user_pw = register_form.user_pw
            )
            user.save()
            return redirect('/')
        else:
            context['forms'] = register_form
            if register_form.errors:
                for value in register_form.errors.values():
                    context['error'] = value
        return render(request, 'user/register.html',context)