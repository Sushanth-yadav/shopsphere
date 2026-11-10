from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('cart/',cart,name='cart'),
    path('add_cart/<int:pk>',add_cart,name='add_cart'),
    path('delete/<int:pk>',delete,name='delete'),
    path('plus/<int:pk>',plus,name='plus'),
    path('minus/<int:pk>',minus,name='minus')
]