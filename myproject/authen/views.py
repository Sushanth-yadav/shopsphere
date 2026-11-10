from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import CartModel
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_(request):
    if request.method=='POST':
        user=authenticate(username=request.POST['uname'],password=request.POST['pasw'])
        if user:
            login(request,user)
            messages.success(request,'successfully logined')
            return redirect('home')
        else:
            messages.error(request,'invalid credentials!')
            return redirect('login_')
    return render(request,'login_.html')

def register(request):
    if request.method=='POST':
        try:
            User.objects.get(username=request.POST['uname'])
            messages.error(request,'username already exists')
            return redirect('register')
        except:
            password = request.POST['pasw']
            if len(password) < 8:
                messages.error(request, 'Password must be at least 8 characters long')
                return redirect('register')
            elif not any(ch.isupper() for ch in password):
                messages.error(request, 'Password must contain at least one uppercase letter')
                return redirect('register')
            elif not any(ch.isdigit() for ch in password):
                messages.error(request, 'Password must contain at least one number')
                return redirect('register')
            elif not any(not ch.isalnum() for ch in password):
                messages.error(request, 'Password must contain at least one special character')
                return redirect('register')
            User.objects.create_user(
                first_name=request.POST['fname'],
                last_name=request.POST['lname'],
                email=request.POST['email'],
                username=request.POST['uname'],
                password=request.POST['pasw'],      
            )
            messages.success(request,'successfully registered')
            return redirect('login_')
    return render(request,'register.html')

@login_required(login_url='login_')
def profile(request):
    cart_count=CartModel.objects.filter(host=request.user).count()
    return render(request,'profile.html',{'cart_count':cart_count})

def logout_(request):
    logout(request)
    return redirect('login_')

def update(request,pk):
    cart_count=CartModel.objects.filter(host=request.user).count()
    return render(request,'update.html',{'cart_count':cart_count})

def reset(request):
    if request.method=="POST":
        if 'oldpass' in request.POST:
            oldpasw=request.POST['oldpass']
            user=authenticate(username=request.user,password=oldpasw)
            if user:
                return render(request,'reset.html',{'new':True})
            else:
                messages.error(request,'invalid old password')
                return redirect('reset')
        if 'newpass' in request.POST:
            new_pass=request.POST["newpass"]
            user=User.objects.get(username=request.user)
            user.set_password(new_pass)
            user.save()
            messages.success(request,'updated successfully')
            return redirect('profile')
    return render(request,'reset.html')

def forgot(request):
    if request.method == 'POST':

        if 'uname' in request.POST:
            uname = request.POST['uname']

            try:
                User.objects.get(username=uname)
                return render(
                    request,
                    'forgot.html',
                    {
                        'show_password_form': True,
                        'uname': uname
                    }
                )

            except:
                messages.error(request, 'Username does not exist')
                return render(request, 'forgot.html')

        elif 'npass' in request.POST:
            uname = request.POST['uname']
            npass = request.POST['npass']

            user = User.objects.get(username=uname)
            user.set_password(npass)
            user.save()

            messages.success(request, 'Password updated successfully')
            return redirect('login_')

    return render(request, 'forgot.html')