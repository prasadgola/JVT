from django.contrib import admin
from django.urls import path, re_path,include
from django.views.generic import TemplateView
from projectapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path('.*', TemplateView.as_view(template_name='index.html'))
]
