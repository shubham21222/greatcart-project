<<<<<<< HEAD
from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','modified_date','is_avaliable')
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(Product,ProductAdmin)
=======
from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','modified_date','is_avaliable')
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(Product,ProductAdmin)
>>>>>>> 1baa7bd3e80870e161f11c7e57ef726649ae0d87
