from django.shortcuts import render,redirect
from authen.models import *
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        cart_count=CartModel.objects.filter(host=request.user).count()
    else:
        cart_count=False
    offer=False
    trend=False
    if 'search' in request.GET:
        search=request.GET['search']
        data=ProductModel.objects.filter(Q(pname__icontains=search)|Q(pcategory__icontains=search)&Q(is_delete=False))
        if len(data)==0:
            messages.error(request,'no product')
            return redirect('home')
    elif 'cat' in request.GET:
        cat=request.GET['cat']
        data=ProductModel.objects.filter(pcategory=cat)
    elif 'offer' in request.GET:
        offer=request.GET['offer']
        data=ProductModel.objects.filter(Q(offers=True) & Q(is_delete=False))
        offer=True
    elif 'trend' in request.GET:
        trend=request.GET['trend']
        data=ProductModel.objects.filter(Q(trending=True) & Q(is_delete=False))
        trend=True
    else:
        data=ProductModel.objects.all()
    category=[]
    for i in ProductModel.objects.all():
        if i.pcategory not in category:
            category.append(i.pcategory)
    return render(request,'home.html',{'data':data,'category':category,'offer':offer,'trend':trend,'home_nav':True,'cart_count':cart_count})


def cart(request):
    cart_count=CartModel.objects.filter(host=request.user).count()
    cart=CartModel.objects.all()
    TA=0
    for i in cart:
        TA+=i.total_price
    return render(request,'cart.html',{'cart':cart,'TA':TA,'cart_count':cart_count})


@login_required(login_url='login_')
def add_cart(request,pk):
    p=ProductModel.objects.get(id=pk)
    try:
        cp=CartModel.objects.get(pname=p.pname,host=request.user)
        cp.quantity+=1
        cp.total_price+=p.price
        cp.save()
        return redirect('home')
    except:
        CartModel.objects.create(
            pname=p.pname,
            price=p.price,
            pcategory=p.pcategory,
            total_price=p.price,
            host=request.user
        )
        return redirect('home')

def delete(request,pk):
    data=CartModel.objects.get(id=pk).delete()
    return redirect('cart')

def plus(request,pk):
    data=CartModel.objects.get(id=pk)
    data.quantity+=1
    data.total_price+=data.price
    data.save()
    return redirect('cart')

def minus(request,pk):
    data=CartModel.objects.get(id=pk)
    if data.quantity>1:
        data.quantity-=1
        data.total_price-=data.price
        data.save()
        return redirect('cart')
    else:
        data.delete()
        return redirect(cart)