from django.contrib import admin
from django.urls import path
from password_generator import views

urlpatterns = [
    path('generate/', views.gen_password, name='gen_password'),
    path('admin/', admin.site.urls),
]