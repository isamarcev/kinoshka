from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path, include
from . import views

app_name = 'cinema'
urlpatterns = [
    path('', views.index, name='cinema'),
    path('cinemas/', staff_member_required(views.CinemasView.as_view()), name='cinemas'),

    path('banners/', views.banners_view, name='banners'),
    path('banners/update_main_banner/', views.update_main_banner, name='update_main_banner'),
    path('banners/update_news_banner/', views.update_news_banner, name='update_news_banner'),
    path('banners/update_background/', views.update_background, name='update_background'),

    path('films/', staff_member_required(views.FilmsView.as_view()), name='films'),
    path('films/create/', views.create_film, name='films_create'),
    path('films/update/<int:pk>/', views.update_film, name='film_update'),

    path('cinemas/create/', views.create_cinema, name='add_cinema'),
    path('cinemas/<int:pk>/update/', views.update_cinema_view, name='update_cinema'),
    path('cinemas/<int:pk>/delete/', views.delete_cinema, name='delete_cinema'),

    path('cinemas/<int:pk>/add-hall/', views.create_hall, name='create_hall'),
    path('cinemas/<int:cinema_pk>/delete-hall/<int:hall_pk>/', views.delete_hall, name='delete_hall'),
    path('cinemas/<int:cinema_pk>/edit-hall/<int:hall_pk>/', views.update_hall_view, name='update_hall'),

    path('news/', staff_member_required(views.NewsView.as_view()), name='news'),
    path('news/create/', views.create_news, name='create_new'),
    path('news/update/<int:pk>/', views.update_news, name='update_new'),

    path('new_or_sale/delete/<int:pk>/', views.delete_new_or_sale, name='delete_new_or_sale'),

    path('sale/', staff_member_required(views.SaleView.as_view()), name='sales'),
    path('sale/create/', views.create_sale, name='create_sale'),
    path('sale/update/<int:pk>/', views.update_sale, name='update_sale'),

    path('pages/', views.pages_view, name='pages'),
    path('pages/create/', views.create_page, name='create_page'),
    path('pages/update/<int:pk>/', views.update_page, name='update_page'),
    path('pages/update_main/<int:pk>/', views.update_main_page, name='update_main_page'),

    path('pages/delete/<int:pk>/', views.update_page, name='delete_page'),
    path('pages/contacts/update/', views.update_contacts, name='update_contacts'),

    path('users/', views.users_view, name='users'),
    path('users/change/<int:pk>/', views.user_change, name='user_change'),
    path('users/delete/<int:pk>/', views.user_delete, name='user_delete'),

    path('mailing/', views.mail_view, name='mailing'),
    path('delete-template/', views.delete_template, name='delete_template'),
    path('mailing/send/', views.send_mail_users, name='send_mail'),

    path('statictics/', views.statistics_view, name='statistics'),

]


