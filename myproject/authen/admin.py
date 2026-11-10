from django.contrib import admin
from .models import*
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model=ProductModel
    list_display=['pname','price','pcategory','pimage']

admin.site.register(ProductModel,ProductAdmin)