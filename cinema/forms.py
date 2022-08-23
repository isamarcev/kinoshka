import datetime

from django import forms
from django.forms import modelformset_factory, HiddenInput

from users.models import CustomUser
from . import models


class CinemaForm(forms.ModelForm):
    name_ru = forms.CharField(required=True, max_length=50, label="Название", widget=forms.TextInput(
        attrs={'class': 'form-control', 'cols': '6', 'rows': '1', 'placeholder': 'Название кинотеатра'}))
    describe_ru = forms.CharField(required=True, label="Описание", widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': '6', 'rows': '6', 'placeholder': 'Описание кинотеатра'}))
    conveniences_ru = forms.CharField(required=True,
                                      label="Удобства",
                                      widget=forms.Textarea(attrs={'class': 'form-control', 'cols': '6',
                                                                   'rows': '6', 'placeholder': 'Описание удобства'}))
    name_uk = forms.CharField(required=True, max_length=50, label="Назва", widget=forms.TextInput(
        attrs={'class': 'form-control', 'cols': '6', 'rows': '1', 'placeholder': 'Назва кинотеатрy'}))
    describe_uk = forms.CharField(required=True, max_length=500, label="Опис", widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': '6', 'rows': '6', 'placeholder': 'Опис кiнотеатрy'}))
    conveniences_uk = forms.CharField(required=True, max_length=500, label="Зручностi", widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': '6', 'rows': '6', 'placeholder': 'Зручностi'}))

    class Meta:
        model = models.Cinema
        fields = ['name_ru', 'describe_ru', 'conveniences_ru', 'name_uk', 'describe_uk',
                  'conveniences_uk', 'logo', 'banner']


class FilmForm(forms.ModelForm):
    title_ru = forms.CharField(max_length=50, label='Название фильма',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'cols': '5', 'rows': '1',
                                                             'placeholder': 'Название фильма'}))
    title_uk = forms.CharField(max_length=50, label='Назва фильму',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'cols': '5', 'rows': '1',
                                                             'placeholder': 'Назва фильму'}))
    describe_ru = forms.CharField(max_length=500, label="Описание", widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': '6', 'rows': '6', 'placeholder': 'Текст'}))
    describe_uk = forms.CharField(max_length=500, label="Опис", widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': '6', 'rows': '6', 'placeholder': 'Текст'}))
    link_trailer = forms.URLField(required=False, label='Ссылка на видео',
                                  widget=forms.URLInput(attrs={'class': 'form-control','cols': 6,
                                                               'rows': 1, 'placeholder': 'Ссылка на трейлер'}))
    f2d = forms.BooleanField(required=False, label='2D', widget=forms.CheckboxInput, label_suffix='')
    f3d = forms.BooleanField(required=False, label='3D', widget=forms.CheckboxInput, label_suffix='')
    IMAX = forms.BooleanField(required=False, label='IMAX', widget=forms.CheckboxInput, label_suffix='')

    class Meta:
        model = models.Film
        fields = ['title_ru', 'title_uk', 'describe_ru', 'describe_uk', 'logo', 'link_trailer',
                  'f2d', 'f3d', 'IMAX']


class HallForm(forms.ModelForm):
    title_ru = forms.CharField(required=True, max_length=50, label='Номер зала',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'cols': '6', 'rows': '1',
                                                             'placeholder': 'Зал №'}))
    title_uk = forms.CharField(required=True, max_length=50, label='Номер залy',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'cols': '6', 'rows': '1',
                                                             'placeholder': 'Зал №'}))
    hall_describe_ru = forms.CharField(required=True, label='Описание зала',
                                       widget=forms.Textarea(attrs={'class': 'form-control', 'cols': '6', 'rows': '6',
                                                                    'placeholder': 'Текст'}))
    hall_describe_uk = forms.CharField(required=True, label='Опис залy',
                                       widget=forms.Textarea(attrs={'class': 'form-control', 'cols': '6', 'rows': '6',
                                                                    'placeholder': 'Текст'}))

    class Meta:
        model = models.Hall
        fields = ['title_ru', 'title_uk', 'hall_describe_ru', 'hall_describe_uk', 'map', 'banner']


class BackgroundBannerForm(forms.ModelForm):
    type = forms.ChoiceField(choices=[('Фото на фоне', 'фото на фоне'), ("Пустой фон", "Пустой фон")], widget=forms.RadioSelect())

    # photo = forms.MultipleChoiceField()
    class Meta:
        model = models.BackgroundBanner
        fields = ['image', 'type']


class BannerBoxForm(forms.ModelForm):
    turning_on = forms.BooleanField(required=False)

    class Meta:
        model = models.BannerBox
        fields = ['turning_on', 'turning_speed']

class BannerForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput, label='')
    url = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control',
                                                                      'placeholder': 'URL'}))
    text = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'cols': 1, 'rows': 1}))
    class Meta:
        model = models.Banner
        fields = ['image', 'url', 'text', 'banner_box']


MainBannerFormSet = modelformset_factory(models.Banner, BannerForm, fields=('image', 'url', 'text', 'banner_box'), extra=0,
                                         can_delete=True)
MainBannerFormSet.deletion_widget = HiddenInput


NewsBannerFormSet = modelformset_factory(models.Banner, BannerForm, fields=('image', 'url', 'banner_box', ), extra=0,
                                         can_delete=True, )
NewsBannerFormSet.deletion_widget = HiddenInput


class SeoForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=400, label='SEO text', widget=forms.TextInput(
        attrs={'class': 'form-control', 'cols': '6', 'rows': '1', 'placeholder': 'Сео Текст'}))
    keyword = forms.CharField(required=True, max_length=400, label='Ключевые слова',
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'cols': '6', 'rows': '1', 'placeholder': 'Ключевые слова'}))
    description = forms.CharField(required=True, max_length=400, label='Описание',
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'cols': '6',
                                                               'rows': '4', 'placeholder': 'Описание'}))
    url = forms.URLField(required=False, label='URL', widget=forms.URLInput(attrs={'class': 'form-control', 'cols': '6',
                                                                                   'rows': '1', 'placeholder': 'URL'}))

    class Meta:
        model = models.Seo
        fields = ['url', 'title', 'keyword', 'description']


class PhotoFormSet(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput, label='')

    class Meta:
        model = models.Photo
        fields = ['image']


PhotoInlineFormset = modelformset_factory(models.Photo, PhotoFormSet, fields=('image',), extra=0, can_delete=True)
PhotoInlineFormset.deletion_widget = HiddenInput


class GaleryForm(forms.ModelForm):
    class Meta:
        model = models.Gallery
        fields = ['title']


class NewsForm(forms.ModelForm):
    title_ru = forms.CharField(max_length=50, label='Название новости',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'cols': '5', 'rows': '1',
                                                             'placeholder': 'Название новости'}))
    title_uk = forms.CharField(max_length=50, label='Назва новини',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'cols': '5', 'rows': '1',
                                                             'placeholder': 'Назва новини'}))
    describe_ru = forms.CharField(max_length=500, label="Описание", widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': '6', 'rows': '6', 'placeholder': 'Текст'}))
    describe_uk = forms.CharField(max_length=500, label="Опис", widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': '6', 'rows': '6', 'placeholder': 'Текст'}))
    m = [('news', 'new'), ('sale', 'sale')]
    news_or_sale = forms.Select(choices=m)
    link = forms.URLField(required=False, label='Ссылка на видео', widget=forms.URLInput(attrs={'class': 'form-control',
                                                                                                'cols': 6, 'rows': 1,
                                                                                                'placeholder': 'Ссылка на YouTube'}))
    is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'type': 'checkbox'}), required=False)
    date = forms.DateField(widget=forms.SelectDateWidget, initial=datetime.date.today)

    class Meta:
        model = models.NewsOrSale
        fields = ['title_ru', 'title_uk', 'describe_ru', 'describe_uk', 'logo', 'link',
                  'news_or_sale', 'is_active', 'date']


class SaleForm(forms.ModelForm):
    title_ru = forms.CharField(max_length=50, label='Название акции',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'cols': '5', 'rows': '1',
                                                             'placeholder': 'Название акции'}))
    title_uk = forms.CharField(max_length=50, label='Назва акции',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'cols': '5', 'rows': '1',
                                                             'placeholder': 'Назва акции'}))
    describe_ru = forms.CharField(max_length=500, label="Описание", widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': '6', 'rows': '6', 'placeholder': 'Текст'}))
    describe_uk = forms.CharField(max_length=500, label="Опис", widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': '6', 'rows': '6', 'placeholder': 'Текст'}))
    m = [('news', 'new'), ('sale', 'sale')]
    news_or_sale = forms.Select(choices=m)
    link = forms.URLField(required=False, label='Ссылка на видео',
                          widget=forms.URLInput(attrs={'class': 'form-control','cols': 6, 'rows': 1,
                                                       'placeholder': 'Ссылка на YouTube'}))
    is_active = forms.BooleanField(required=False)
    date = forms.DateField(widget=forms.SelectDateWidget, initial=datetime.date.today)

    class Meta:
        model = models.NewsOrSale
        fields = ['title_ru', 'title_uk', 'describe_ru', 'describe_uk', 'logo', 'link',
                  'news_or_sale', 'is_active', 'date']


class PagesForm(forms.ModelForm):
    title_ru = forms.CharField(max_length=50, label='Название страницы',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'cols': '5', 'rows': '1',
                                                             'placeholder': 'Название страницы'}))
    title_uk = forms.CharField(max_length=50, label='Назва сторiнки',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'cols': '5', 'rows': '1',
                                                             'placeholder': 'Назва сторiнки'}))
    describe_ru = forms.CharField(label="Описание", widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': '6', 'rows': '6', 'placeholder': 'Текст'}))
    describe_uk = forms.CharField(label="Опис", widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': '6', 'rows': '6', 'placeholder': 'Текст'}))
    status = forms.BooleanField(required=False)

    class Meta:
        model = models.Pages
        fields = ['title_ru', 'title_uk', 'describe_ru', 'describe_uk', 'logo', 'status']


class MainPageForm(forms.ModelForm):
    phone1 = forms.CharField(max_length=12, label='Название страницы',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'cols': '3', 'rows': '1',
                                                             'placeholder': 'Название страницы'}))
    phone2 = forms.CharField(max_length=12, label='Назва сторiнки',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'cols': '3', 'rows': '1',
                                                             'placeholder': 'Назва сторiнки'}))
    seo_text_ru = forms.CharField(max_length=500, label="Описание", widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': '12', 'rows': '6', 'placeholder': 'Текст CEO'}))
    seo_text_uk = forms.CharField(max_length=500, label="Опис", widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': '12', 'rows': '6', 'placeholder': 'Текст CEO'}))
    status = forms.BooleanField(required=False)

    class Meta:
        model = models.Pages
        fields = ['phone1', 'phone2', 'seo_text_ru', 'seo_text_uk', 'status']


class ContactsForm(forms.ModelForm):
    cinema_name = forms.CharField(max_length=50, label='Название кинотеатра', widget=forms.TextInput(
        attrs={'class': 'form-control', 'cols': '3', 'rows': '1', 'placeholder': 'Название кинотеатра'}))
    address = forms.CharField(label='Адресс кинотеатра', widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': '6', 'rows': '4', 'placeholder': 'Адресс кинотеатра'}))
    coordinates = forms.URLField(label='Координаты для карты', widget=forms.URLInput(
        attrs={'class': 'form-control', 'cols': '6', 'rows': '1', 'placeholder': 'Координаты для карты'}))
    status = forms.BooleanField(required=False, widget=forms.CheckboxInput)

    class Meta:
        model = models.Contacts
        fields = ['cinema_name', 'address', 'coordinates', 'logo', 'status']


ContactsFormSet = modelformset_factory(models.Contacts, ContactsForm, fields=('cinema_name', 'address', 'coordinates', 'logo', 'status',),
                                       extra=0)
ContactsFormSet.deletion_widget = HiddenInput


class CustomUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label="Имя", widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Имя'
    }))
    last_name = forms.CharField(max_length=50, label="Фамилия", widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Фамилия'
    }))
    username = forms.CharField(max_length=50, label="Псевдоним", widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Псевдоним'
    }))
    email = forms.EmailField(max_length=50, label="Email", widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Email'
    }))
    address = forms.CharField(max_length=50, label="Адресс", widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Адресс'
    }))
    password = forms.CharField(max_length=50, label="Parol", widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Parol'
    }))
    sex = forms.ChoiceField(choices=[('m', 'male'), ('f', 'female')], widget=forms.RadioSelect(attrs={
        'width': '20px',
    }))
    language = forms.ChoiceField(choices=[('r', 'Russian'), ('u', 'UA')], widget=forms.RadioSelect())
    number_of_card = forms.IntegerField(max_value=9999999999999999, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    phone = forms.CharField(max_length=13, widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    birthday = forms.DateField(widget=forms.SelectDateWidget)
    password2 = forms.CharField(max_length=50, label="Повторить пароль", widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Повторить пароль', 'cols': '5',
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'address', 'password',
                  'number_of_card', 'language', 'sex', 'phone', 'birthday', 'city', 'password2']



class SessionForm(forms.ModelForm):

    class Meta:
        model = models.Session
        fields = ['place',]


class HtmlTemplateForm(forms.ModelForm):

    class Meta:
        model = models.HtmlTemplate
        fields = ['file',]