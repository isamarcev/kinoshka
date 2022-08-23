from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('accounts/login/', views.LoginUser.as_view(), name='login'),
    path('accounts/register/', views.RegisterUser.as_view(), name='register'),

    # path('home/', views.LoginUser.as_view(), name='login')

]


