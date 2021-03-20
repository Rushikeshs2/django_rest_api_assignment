from django.contrib import admin
from django.urls import path,include
from myapp import views 
from .views import adviser_api,adviser_create

urlpatterns = [
    path('adviser_api/',   views.adviser_api,name='adviser_api' ),
    path('createadviser/',views.adviser_create,name='createadviser')
]