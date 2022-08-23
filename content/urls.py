from django.urls import path, include
from . import views

app_name = 'content'
urlpatterns = [
    path('', views.main_page, name='main'),

    path('afisha/', views.afisha_view, name='afisha'),
    path('soon/', views.soon_view, name='soon'),

    path('shedule/', views.shedule_view, name='shedule'),
    path('shedule/cinema-up/', views.shedule_view_cinema_up, name='shedule_cinema_up'),

    path('buy-tickets/<int:pk>/', views.buy_tickets, name='buy-tickets'),
    path('bought/', views.bought_ticket, name='bought-tickets'),

    path('film/<int:pk>/', views.film_view, name='film'),
    # path('films/<int:pk>/', views.films_view, name='film'),

    path('cinemas/', views.cinemas_view, name='cinemas'),
    path('cinemas/cinema/<int:pk>/', views.cinema_view, name='cinema'),
    path('cinemas/cinema/hall/<int:pk>/', views.hall_view, name='hall'),

    path('sales/', views.sales_view, name='sales'),

    path('sales/<int:pk>/', views.sale_view, name='sale'),

    path('news/', views.news_view, name='news'),
    path('news/<int:pk>/', views.new_view, name='new'),

    path('coffee-bar/', views.coffee_bar, name='coffee'),
    path('vip-hall/', views.vip_hall, name='vip'),
    path('adv/', views.adversting_view, name='adv'),
    path('mobile/', views.mobile_view, name='mob'),
    path('contacts/', views.contacts_view, name='contacts'),

    # path('home/', views.LoginUser.as_view(), name='login')

]


