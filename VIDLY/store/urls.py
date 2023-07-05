<<<<<<< HEAD

from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.store,name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),

    

] 
=======

from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.store,name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),

    

] 
>>>>>>> 1baa7bd3e80870e161f11c7e57ef726649ae0d87
