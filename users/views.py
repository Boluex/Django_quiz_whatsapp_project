from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from.models import profile
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from.forms import *

# Create your views here.

def sign_in(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('login')
    return render(request,'users/login.html')

def sign_up(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        email=request.POST.get('email').lower()
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return HttpResponse('user exists')
            else:
                new_user=User(username=username,password=password1,email=email)
                new_user.save()
                login(request,new_user)
                return redirect('redirect')
        return redirect('register')
    return render(request,'users/register.html')



# def sign_out(request):
#     logout(request)
#     return redirect('login')

# def user_profile(request):
#     get_user_profile=profile.objects.get(user=request.user)
#     context={
#         'user-data':get_user_profile
#     } 
#     return JsonResponse(context)

# def update_user(request):
#     u_form=user_form()
#     if request.method=='POST':
#         u_form=user_form(request.POST,instance=request.user)
#         if u_form.is_valid():
#             u_form.save()
#             return  redirect('login')
#         return  redirect('login')
#         # return HttpResponse('Error while updating user')
#     form={
#         'u_form':u_form,

#     }
#     return render(request,'users/update_user.html',form)




# Reset aacoount

def reset_account(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        if User.objects.filter(username=request.user.username,email=email).exists():
            get_user=User.objects.get(username=request.user.username,email=email)
            get_user.set_password(password)
            return redirect('login')
        return redirect("update_user")
    return render(request,'users/update_user.html')