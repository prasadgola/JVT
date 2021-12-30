from django.contrib import admin
from django.urls import path
from onemoreapp import views

urlpatterns = [
    path('login',views.user_login, name = 'nobulshit'),
    path('ppl',views.ppl, name = 'ppl'),
    path('show',views.show, name = 'show'),
    path('allconnected',views.allconnected, name = 'allconnected'),

]