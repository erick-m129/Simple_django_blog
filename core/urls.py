from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
        path('', views.login_user, name='login'),
        path('register/', views.register, name='register'),
    ]