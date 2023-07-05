<<<<<<< HEAD
from django.contrib import admin
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name','slug')

admin.site.register(Category,CategoryAdmin)
=======
from django.contrib import admin
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name','slug')

admin.site.register(Category,CategoryAdmin)
>>>>>>> 1baa7bd3e80870e161f11c7e57ef726649ae0d87
