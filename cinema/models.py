import datetime
import os.path
import time
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import JSONField
from django.conf import settings
from django.urls import reverse
from django.utils import timezone


class Cinema(models.Model):
    name = models.CharField(max_length=32, verbose_name="Название кинотеатра", unique=True)
    describe = models.TextField(verbose_name="Описание")
    conveniences = models.TextField(verbose_name="Удобства", blank=True, null=True)
    logo = models.ImageField(upload_to='cinema/', blank=True, null=True, verbose_name="Логотип")
    banner = models.ImageField(upload_to='cinema/', blank=True, null=True, verbose_name="Фото верхнего баннера")
    pictures = models.ForeignKey('Gallery', on_delete=models.CASCADE, verbose_name="Галерея картинок", null=True, blank=True)
    seo = models.OneToOneField('Seo', on_delete=models.CASCADE, verbose_name="СЕО блок", null=True, blank=True)

    @staticmethod
    def get_absolute_url():
        return reverse('cinema:cinemas')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Кинотеатры'
        verbose_name = 'Кинотеатр'


class Hall(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Кинотеатр")
    title = models.CharField(max_length=30, blank=True, unique=True, verbose_name="Название зала")
    hall_describe = models.TextField(null=True, blank=True, verbose_name="Описание зала")
    map = models.ImageField(upload_to='hall/', blank=True, null=True, verbose_name="Карта зала")
    banner = models.ImageField(upload_to='hall/', blank=True, null=True, verbose_name="Холл баннер")
    pictures = models.ForeignKey("Gallery", on_delete=models.CASCADE, verbose_name="Картинки")
    seo = models.OneToOneField("Seo", on_delete=models.CASCADE, verbose_name="СЕО блок")
    places = models.JSONField(null=True, blank=True, verbose_name="Места", max_length=10000)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Залы'
        verbose_name = 'Зал'

    def __str__(self):
        return str(self.title)


class Session(models.Model):
    name = models.CharField(max_length=500, verbose_name='Номер сеанса')
    date = models.DateTimeField(null=True, blank=True, verbose_name='Дата сеанса')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Номер зала')
    film = models.ForeignKey('Film', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Название фильма')
    price = models.IntegerField(null=True, blank=True, verbose_name='Price')
    place = models.JSONField(null=True, blank=True, max_length=10000)

    def __str__(self):
        return f'({self.name}, {self.hall.title})'

    class Meta:
        verbose_name_plural = 'Сеансы'
        verbose_name = 'Сеанс'

    def set_place(self):
        place = self.hall.places
        return place


class Film(models.Model):
    title = models.CharField(max_length=32, null=True, blank=True, verbose_name='Название фильма', unique=True)
    describe = models.TextField(max_length=200, null=True, blank=True, verbose_name='Описание фильма')
    link_trailer = models.URLField(null=True, blank=True, verbose_name='Ссылка на фильм')
    f2d = models.BooleanField(null=True, default=False, verbose_name='2D')
    f3d = models.BooleanField(null=True, default=False, verbose_name='3D')
    IMAX = models.BooleanField(null=True, default=False, verbose_name='IMAX')
    date_of_premier = models.DateTimeField(null=True, blank=True, verbose_name='Дата премьеры')
    seo = models.OneToOneField('Seo', on_delete=models.PROTECT, null=True, blank=True, verbose_name='SEO блок')
    logo = models.ImageField(upload_to=f'film/', null=True, verbose_name='Логотип фильма', blank=True)
    pictures = models.ForeignKey('Gallery', on_delete=models.CASCADE, null=True, verbose_name="Картинки")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Фильмы'
        verbose_name = 'Фильм'


class Seo(models.Model):
    title = models.CharField(max_length=32, null=True, blank=True, verbose_name='Заголовок СЕО', unique=True)
    keyword = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    url = models.URLField(null=True, verbose_name='URL', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'СЕО блоки'
        verbose_name = 'СЕО блок'


class Gallery(models.Model):
    title = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Галереи'
        verbose_name = 'Галерея'


class Photo(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to=f'gallery/', blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Фотографии'
        verbose_name = 'Фото'


class BackgroundBanner(models.Model):
    image = models.ImageField(upload_to='backgroundbanner/', null=True, blank=True, verbose_name='Фото на фоне')
    type = models.CharField(max_length=32, null=True, blank=True,
                            choices=[('Фото на фоне', 'фото на фоне'), ("Пустой фон", "Пустой фон")])
    title = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.title


class BannerBox(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    ts = [('3', '3'),('5', '5'), ('10', '10')]
    nm = [('news', 'new'), ('main', 'main')]
    turning_speed = models.CharField(max_length=32, choices=ts, default='3')
    turning_on = models.BooleanField(default=False, blank=True, null=True)
    news_or_main = models.CharField(max_length=32,choices=nm, default='main')
    status = models.BooleanField(null=True, blank=True, default=True)


class Banner(models.Model):
    banner_box = models.ForeignKey(BannerBox, on_delete=models.CASCADE, verbose_name='BannerBox', null=True, blank=True)
    image = models.ImageField(upload_to='banner_box/')
    url = models.URLField(null=True)
    text = models.TextField(null=True, max_length=500)


class MainPage(models.Model):
    title = models.CharField(max_length=40, default='Главная страница')
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15)
    seo_text = models.TextField(max_length=500)
    seo = models.ForeignKey(Seo, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Contacts(models.Model):
    cinema_name = models.CharField(max_length=40, null=True, verbose_name='Название кинотеатра')
    address = models.CharField(max_length=500, null=True, default='Не указан адресс')
    coordinates = models.URLField(max_length=1000, verbose_name='Координаты кинотеатра')
    logo = models.ImageField(upload_to='contact/', null=True)
    seo = models.OneToOneField(Seo, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return self.cinema_name


class Pages(models.Model):
    title = models.CharField(max_length=50, null=True, default='Не указано название страницы')
    describe = models.TextField(null=True)
    logo = models.ImageField(upload_to='pages/')
    pictures = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True)
    seo = models.OneToOneField(Seo, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)
    can_delete = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class NewsOrSale(models.Model):
    date = models.DateField(verbose_name='Дата публикации', null=True)
    title = models.CharField(max_length=50, help_text='Название новости')
    describe = models.TextField(null=True)
    logo = models.ImageField(upload_to='news_or_sale/', null=True, blank=True)
    pictures = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True)
    link = models.URLField(verbose_name="Ссылка на новость",null=True)
    status = models.BooleanField(default=True,null=True)
    m = [('news', 'new'), ('sale', 'sale')]
    news_or_sale = models.CharField(max_length=32,choices=m,null=True, default='news')
    seo = models.OneToOneField(Seo, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title



class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    places = models.CharField(max_length=500, null=True, blank=True)

class HtmlTemplate(models.Model):
    file = models.FileField(upload_to='html_template/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

    def filename(self):
        return os.path.basename(self.file.name)

