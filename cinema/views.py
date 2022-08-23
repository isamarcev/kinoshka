import datetime

from bs4 import BeautifulSoup
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_deny
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from .tasks import mailing, fibon
from users.models import CustomUser
from .forms import *
from .models import Cinema, Film, NewsOrSale, Hall, Seo, Photo, Gallery, MainPage, Contacts, Pages, BannerBox, Banner, \
    BackgroundBanner, Session
from django.contrib import messages


def index(request):
    return render(request, 'cinema/layout/base.html')


@staff_member_required
def banners_view(request):
    banners = BannerBox.objects.all()
    backgroundbanner = BackgroundBanner.objects.first()
    backgroundbanner_form = BackgroundBannerForm(instance=backgroundbanner)
    for i in banners:
        if i.news_or_main == 'main':
            main_qs = i.banner_set.all()
            main_banner_form = BannerBoxForm(instance=i, prefix='main')
        elif i.news_or_main == 'news':
            news_banner_form = BannerBoxForm(instance=i, prefix='news')
            news_qs = i.banner_set.all()
    main_banner_formset = MainBannerFormSet(queryset=main_qs, prefix='main_formset')
    news_banner_formset = NewsBannerFormSet(queryset=news_qs, prefix='news_formset')
    context = {
        'main_banner': main_banner_form,
        'news_banner': news_banner_form,
        'backgroundbanner': backgroundbanner_form,
        'main_banner_formset': main_banner_formset,
        'news_banner_formset': news_banner_formset,
    }

    return render(request, 'cinema/banners/banners.html', context=context)

@staff_member_required
def update_main_banner(request):
    main_banner = BannerBox.objects.get(news_or_main='main')
    if request.method == 'POST':
        main = BannerBoxForm(request.POST, request.FILES, instance=main_banner, prefix='main')
        if main.is_valid():
            main.save()
        main_banner_formset = MainBannerFormSet(request.POST, request.FILES, prefix='main_formset')
        if main_banner_formset.is_valid():
            main_banner_formset.save(commit=False)
            for form in main_banner_formset.new_objects:
                if form.image:
                    form.banner_box = main.instance
                    form.save()
            for i in main_banner_formset.deleted_objects:
                i.delete()
            for form in main_banner_formset.changed_objects:
                    form[0].banner_box = main.instance
                    form[0].save()
            main_banner_formset.save()
        return HttpResponseRedirect(reverse_lazy('cinema:banners'))
    return HttpResponseRedirect('cinema/banners/')


@staff_member_required
def update_news_banner(request):
    news_banner = BannerBox.objects.get(news_or_main='news')
    if request.method == 'POST':
        news = BannerBoxForm(request.POST, request.FILES, instance=news_banner, prefix='news')
        if news.is_valid():
            news.save()
        news_banner_formset = NewsBannerFormSet(request.POST, request.FILES, prefix='news_formset')
        if news_banner_formset.is_valid():
            news_banner_formset.save(commit=False)
            for form in news_banner_formset.new_objects:
                if form.image:
                    form.banner_box = news.instance
                    form.save()
            for i in news_banner_formset.deleted_objects:
                i.delete()
            for form in news_banner_formset.changed_objects:
                    form[0].banner_box = news.instance
                    form[0].save()
            news_banner_formset.save()
        return HttpResponseRedirect(reverse_lazy('cinema:banners'))
    return HttpResponseRedirect('cinema/banners/')


@staff_member_required
def update_background(request):
    backgroundbanner = BackgroundBanner.objects.first()
    if request.method == 'POST':
        backgroundbanner_form = BackgroundBannerForm(request.POST, request.FILES, instance=backgroundbanner)
        # print(backgroundbanner_form.is_valid(), backgroundbanner_form, backgroundbanner_form.instance)
        if backgroundbanner_form.is_valid():
            backgroundbanner_form.instance.save()
        else:
            print(backgroundbanner_form.errors)
    return HttpResponseRedirect(reverse_lazy('cinema:banners'))



class CinemasView(TemplateView):
    template_name = 'cinema/cinemas/cinema_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cinemas'] = Cinema.objects.all()
        return context


class FilmsView(TemplateView):
    template_name = 'cinema/films/films_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = Film.objects.all()
        return context


class NewsView(ListView):
    model = NewsOrSale
    template_name = 'cinema/news/news_list.html'
    context_object_name = 'news'

    def get_queryset(self):
        return NewsOrSale.objects.filter(news_or_sale='news')


class SaleView(ListView):
    model = NewsOrSale
    template_name = 'cinema/sale/sale_list.html'
    context_object_name = 'sale'

    def get_queryset(self):
        return NewsOrSale.objects.filter(news_or_sale='sale')


class CreateNewsView(CreateView):
    model = NewsOrSale
    template_name = 'cinema/news/news_create.html'


class CreateCinemaView(CreateView):
    form_class = CinemaForm
    template_name = 'cinema/cinemas/cinema_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['halls'] = Cinema.objects.prefetch_related('hall_set').all()

        return context


@staff_member_required
def create_film(request):
    if request.method == 'POST':
        film = FilmForm(request.POST, request.FILES)
        seo = SeoForm(request.POST)
        formset = PhotoInlineFormset(request.POST, request.FILES)
        print(film.is_valid(), film.errors, seo.is_valid(), formset.is_valid())
        if film.is_valid() and seo.is_valid() and formset.is_valid():
            film.save(commit=False)
            gallery = Gallery.objects.create(title=film.cleaned_data['title_ru'])
            gallery.save()
            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.gallery = gallery
                    form.save()
            film.instance.pictures = gallery
            seo.save()
            film.instance.seo = seo.instance
            film.save()
            return HttpResponseRedirect('/cinema/films/')
    else:
        data = {'form-TOTAL_FORMS': '0',
                'form-INITIAL_FORMS': '0',
                }
        film = FilmForm
        seo = SeoForm
        formset = PhotoInlineFormset(data)
    return render(request, 'cinema/films/film_create.html', {'film': film, 'seo': seo, 'formset': formset})


@staff_member_required
def update_film(request, pk):
    obj = get_object_or_404(Film, pk=pk)
    seo_c = obj.seo
    g = get_object_or_404(Gallery, id=obj.pictures.id)
    qs = g.photo_set.all()
    if request.method == 'POST':
        print(request.POST)
        film = FilmForm(request.POST or None, request.FILES or None, instance=obj)
        seo = SeoForm(request.POST or None, instance=seo_c)
        formset = PhotoInlineFormset(request.POST or None, request.FILES or None, queryset=qs)
        print(film.is_valid(),seo.is_valid(),  formset.is_valid())
        print(film.errors,seo.errors,  formset.errors)

        if film.is_valid() and seo.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.gallery = g
                i.save()
            for i in formset.changed_objects:
                i[0].save()
            formset.save()
            seo_c.save()
            film.save()
            return HttpResponseRedirect('/cinema/films/')
        else:
            return HttpResponse('Что то пошло не так!!!')
    film = FilmForm(instance=obj)
    seo = SeoForm(instance=seo_c)
    formset = PhotoInlineFormset(queryset=qs)
    context = {'film': film, 'seo': seo, 'formset': formset}
    return render(request, 'cinema/films/film_update.html', context)


@staff_member_required
def create_cinema(request):
    if request.method == 'POST':
        cinemas = CinemaForm(request.POST, request.FILES)
        seo = SeoForm(request.POST)
        formset = PhotoInlineFormset(request.POST, request.FILES)
        print(formset)
        if cinemas.is_valid() and seo.is_valid() and formset.is_valid():
            cinemas.save(commit=False)
            gallery = Gallery.objects.create(title=cinemas.cleaned_data['name_ru'])
            gallery.save()
            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.gallery = gallery
                    form.save()
            cinemas.instance.pictures = gallery
            seo.save()
            cinemas.instance.seo = seo.instance
            cinemas.save()
            return HttpResponseRedirect('/cinema/cinemas/')

    else:
        data = {'form-TOTAL_FORMS': '0',
                'form-INITIAL_FORMS': '0',
                }
        cinemas = CinemaForm
        seo = SeoForm
        formset = PhotoInlineFormset(data)
    return render(request, 'cinema/cinemas/cinema_add.html', {'cinemas': cinemas, 'seo': seo, 'formset': formset})


@staff_member_required
def update_cinema_view(request, pk):
    obj = get_object_or_404(Cinema, pk=pk)
    seo_c = obj.seo
    g = get_object_or_404(Gallery, id=obj.pictures.id)
    qs = g.photo_set.all()
    if request.method == 'POST':
        cinemas = CinemaForm(request.POST or None, request.FILES or None, instance=obj)
        seo = SeoForm(request.POST or None, instance=seo_c)
        formset = PhotoInlineFormset(request.POST or None, request.FILES or None, queryset=qs)
        if cinemas.is_valid() and seo.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.gallery = g
                i.save()
            for i in formset.changed_objects:
                i[0].save()
            formset.save()
            seo_c.save()
            cinemas.save()
            return HttpResponseRedirect('/cinema/cinemas/')
        else:
            return HttpResponse('Что то пошло не так!!!')
    cinemas = CinemaForm(instance=obj)
    seo = SeoForm(instance=seo_c)
    halls = obj.hall_set.all()
    formset = PhotoInlineFormset(queryset=qs)
    context = {'cinemas': cinemas, 'seo': seo, 'formset': formset, 'halls': halls}
    return render(request, 'cinema/cinemas/cinema_update_def.html', context)


@staff_member_required
def delete_cinema(request, pk):
    if request.method == 'POST':
        obj = get_object_or_404(Cinema, pk=pk)
        obj.delete()
        print('Done')
    return HttpResponseRedirect(reverse_lazy('cinema:cinemas'))


@staff_member_required
def create_hall(request, pk):
    if request.method == 'POST':
        halls = HallForm(request.POST, request.FILES)
        seo = SeoForm(request.POST)
        formset = PhotoInlineFormset(request.POST, request.FILES)
        if halls.is_valid() and seo.is_valid() and formset.is_valid():
            halls.save(commit=False)
            cinema = Cinema.objects.get(pk=pk)
            gallery = Gallery.objects.create(title=f"{halls.cleaned_data['title_ru']} / {cinema.name}")
            gallery.save()
            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.gallery = gallery
                    form.save()
            halls.instance.pictures = gallery
            halls.instance.cinema = cinema
            seo.save()
            halls.instance.seo = seo.instance

            halls.save()
            return HttpResponseRedirect(reverse_lazy('cinema:cinemas'))
    else:
        data = {'form-TOTAL_FORMS': '0',
                'form-INITIAL_FORMS': '0', }
        halls = HallForm
        seo = SeoForm
        formset = PhotoInlineFormset(data)
    return render(request, 'cinema/hall/hall_add.html', {'halls': halls, 'seo': seo, 'formset': formset})


@staff_member_required
def delete_hall(request, cinema_pk, hall_pk):
    cinema = get_object_or_404(Cinema, pk=cinema_pk)
    hall = get_object_or_404(Hall, pk=hall_pk)
    if request.method == 'POST':
        hall.delete()
        print('Done')
    return HttpResponseRedirect(reverse_lazy('cinema:cinemas'))


@staff_member_required
def update_hall_view(request, cinema_pk, hall_pk):
    hall = Cinema.objects.get(pk=cinema_pk).hall_set.get(pk=hall_pk)
    seo_c = hall.seo
    g = get_object_or_404(Gallery, id=hall.pictures.id)
    qs = g.photo_set.all()
    if request.method == 'POST':
        halls = HallForm(request.POST or None, request.FILES or None, instance=hall)
        seo = SeoForm(request.POST or None, instance=seo_c)
        formset = PhotoInlineFormset(request.POST or None, request.FILES or None, queryset=qs)
        if halls.is_valid() and seo.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.gallery = g
                i.save()
            for i in formset.changed_objects:
                i[0].save()
            formset.save()
            seo_c.save()
            halls.save()
            return HttpResponseRedirect('/cinema/cinemas/')
        else:
            return HttpResponse('Что то пошло не так!!!')
    halls = HallForm(instance=hall)
    seo = SeoForm(instance=seo_c)
    formset = PhotoInlineFormset(queryset=qs)
    context = {'seo': seo, 'formset': formset, 'halls': halls}
    return render(request, 'cinema/hall/hall_edit.html', context)


@staff_member_required
def create_news(request):
    if request.method == 'POST':
        news_or_sales = NewsForm(request.POST, request.FILES)
        seo = SeoForm(request.POST)
        formset = PhotoInlineFormset(request.POST, request.FILES)
        if news_or_sales.is_valid() and seo.is_valid() and formset.is_valid():
            news_or_sales.save(commit=False)
            gallery = Gallery.objects.create(title=news_or_sales.cleaned_data['title_ru'])
            gallery.save()
            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.gallery = gallery
                    form.save()
            news_or_sales.instance.pictures = gallery
            seo.save()
            news_or_sales.instance.seo = seo.instance
            news_or_sales.save()
            return HttpResponseRedirect('/cinema/news/')
    else:
        data = {'form-TOTAL_FORMS': '0',
                'form-INITIAL_FORMS': '0',
                }
        news_or_sales = NewsForm(initial={'news_or_sale': 'new'})
        seo = SeoForm
        formset = PhotoInlineFormset(data)
    return render(request, 'cinema/news/news_create.html', {'news_or_sales': news_or_sales, 'seo': seo, 'formset': formset})


@staff_member_required
def update_news(request, pk):
    new = get_object_or_404(NewsOrSale, pk=pk)
    new_seo = new.seo
    g = get_object_or_404(Gallery, id=new.pictures.id)
    qs = g.photo_set.all()
    if request.method == 'POST':
        news = NewsForm(request.POST or None, request.FILES or None, instance=new)
        seo = SeoForm(request.POST or None, instance=new_seo)
        formset = PhotoInlineFormset(request.POST or None, request.FILES or None, queryset=qs)
        if news.is_valid() and seo.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.gallery = g
                i.save()
            for i in formset.changed_objects:
                i[0].save()
            formset.save()
            new_seo.save()
            news.save()
            return HttpResponseRedirect('/cinema/news/')
        else:
            return HttpResponse('Что то пошло не так!!!')
    news = NewsForm(instance=new)
    seo = SeoForm(instance=new_seo)
    formset = PhotoInlineFormset(queryset=qs)
    context = {'seo': seo, 'formset': formset, 'news_or_sales': news}
    return render(request, 'cinema/news/news_update.html', context)


@staff_member_required
def create_sale(request):
    if request.method == 'POST':
        news_or_sales = SaleForm(request.POST, request.FILES)
        seo = SeoForm(request.POST)
        formset = PhotoInlineFormset(request.POST, request.FILES)
        if news_or_sales.is_valid() and seo.is_valid() and formset.is_valid():
            news_or_sales.save(commit=False)
            gallery = Gallery.objects.create(title=news_or_sales.cleaned_data['title_ru'])
            gallery.save()
            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.gallery = gallery
                    form.save()
            news_or_sales.instance.pictures = gallery
            seo.save()
            news_or_sales.instance.seo = seo.instance
            news_or_sales.save()
            return HttpResponseRedirect('/cinema/sale/')
    else:
        data = {'form-TOTAL_FORMS': '0',
                'form-INITIAL_FORMS': '0',
                }
        news_or_sales = SaleForm(initial={'news_or_sale': 'sale'})
        seo = SeoForm
        formset = PhotoInlineFormset(data)
    return render(request, 'cinema/sale/sale_create.html', {'news_or_sales': news_or_sales, 'seo': seo, 'formset': formset})


@staff_member_required
def update_sale(request, pk):
    new = get_object_or_404(NewsOrSale, pk=pk)
    new_seo = new.seo
    g = get_object_or_404(Gallery, id=new.pictures.id)
    qs = g.photo_set.all()
    if request.method == 'POST':
        news = SaleForm(request.POST or None, request.FILES or None, instance=new)
        seo = SeoForm(request.POST or None, instance=new_seo)
        formset = PhotoInlineFormset(request.POST or None, request.FILES or None, queryset=qs)
        if news.is_valid() and seo.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.gallery = g
                i.save()
            for i in formset.changed_objects:
                i[0].save()
            formset.save()
            new_seo.save()
            news.save()
            return HttpResponseRedirect('/cinema/sale/')
        else:
            return HttpResponse('Что то пошло не так!!!')
    news = SaleForm(instance=new)
    seo = SeoForm(instance=new_seo)
    formset = PhotoInlineFormset(queryset=qs)
    context = {'seo': seo, 'formset': formset, 'news_or_sales': news}
    return render(request, 'cinema/sale/sale_update.html', context)


@staff_member_required
def delete_new_or_sale(request, pk):
    obj = get_object_or_404(NewsOrSale, pk=pk)
    if request.method == 'POST':
        obj.delete()
        print('Done')
    if obj.news_or_sale == 'news':
        return HttpResponseRedirect(reverse_lazy('cinema:news'))
    else:
        return HttpResponseRedirect(reverse_lazy('cinema:sales'))


@staff_member_required
def pages_view(request):
    main_page = MainPage.objects.first()
    pages = Pages.objects.all()
    context = {
        'main_page': main_page,
        'pages': pages,
    }
    return render(request, 'cinema/pages/pages_list.html', context)


@staff_member_required
def create_page(request):
    if request.method == 'POST':
        page = PagesForm(request.POST, request.FILES)
        seo = SeoForm(request.POST)
        formset = PhotoInlineFormset(request.POST, request.FILES)
        if page.is_valid() and seo.is_valid() and formset.is_valid():
            page.save(commit=False)
            gallery = Gallery.objects.create(title=page.cleaned_data['title_ru'])
            gallery.save()
            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.gallery = gallery
                    form.save()
            page.instance.pictures = gallery
            seo.save()
            page.instance.seo = seo.instance
            page.save()
            return HttpResponseRedirect('/cinema/pages/')
    else:
        data = {'form-TOTAL_FORMS': '0',
                'form-INITIAL_FORMS': '0',
                }
        page = PagesForm
        seo = SeoForm
        formset = PhotoInlineFormset(data)
        context = {
            'page': page, 'seo': seo, 'formset': formset
        }
        return render(request, 'cinema/pages/page_new.html', context)


@staff_member_required
def update_page(request, pk):
    page = get_object_or_404(Pages, pk=pk)
    page_seo = page.seo
    g = get_object_or_404(Gallery, id=page.pictures.id)
    qs = g.photo_set.all()
    if request.method == 'POST':
        page = PagesForm(request.POST or None, request.FILES or None, instance=page)
        seo = SeoForm(request.POST or None, instance=page_seo)
        formset = PhotoInlineFormset(request.POST or None, request.FILES or None, queryset=qs)
        if page.is_valid() and seo.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                if i.image:
                    i.gallery = g
                    i.save()
            for i in formset.changed_objects:
                if i.instance.image:
                    i[0].save()
            formset.save()
            page_seo.save()
            page.save()
            return HttpResponseRedirect('/cinema/pages/')
        else:
            return HttpResponse('Что то пошло не так!!!')
    pages = PagesForm(instance=page)
    seo = SeoForm(instance=page_seo)
    formset = PhotoInlineFormset(queryset=qs)
    context = {'seo': seo, 'formset': formset, 'page': pages}
    return render(request, 'cinema/pages/page_update.html', context)


@staff_member_required
def delete_page(request, id):
    page = Pages.objects.get(pk=id)
    page.delete()
    return HttpResponseRedirect(reverse_lazy('cinema:pages'))


@staff_member_required
def update_main_page(request, pk):
    page = MainPage.objects.get(pk=pk)
    page_seo = page.seo
    if request.method == 'POST':
        page = MainPageForm(request.POST or None, request.FILES or None, instance=page)
        seo = SeoForm(request.POST or None, instance=page_seo)
        if page.is_valid() and seo.is_valid():
            page_seo.save()
            page.save()
            return HttpResponseRedirect('/cinema/pages/')
        else:
            return HttpResponse('Что то пошло не так!!!')
    pages = MainPageForm(instance=page)
    seo = SeoForm(instance=page_seo)
    context = {'seo': seo, 'page': pages}
    return render(request, 'cinema/pages/main_page_update.html', context)


@staff_member_required
def update_contacts(request):
    contact = Contacts.objects.all()
    seo_contacts = contact.first().seo
    if request.method == 'POST':
        seo = SeoForm(request.POST, instance=seo_contacts)
        formset = ContactsFormSet(request.POST, request.FILES, queryset=contact)
        print(formset.is_valid(), formset.errors)
        if formset.is_valid() and seo.is_valid():
            formset.save(commit=False)
            seo.save(commit=False)
            for i in formset.new_objects:
                if i.logo:
                    i.save()
            for i in formset.changed_objects:
                print(i)
                i[0].save()
            seo.save()
            formset.save()
            return HttpResponseRedirect('/cinema/pages/')
    else:
        seo = SeoForm(instance=seo_contacts)
        formset = ContactsFormSet(queryset=contact)
    return render(request, 'cinema/pages/contacts_update.html', {'seo':seo, 'formset': formset, 'contact': contact})


@staff_member_required
def users_view(request):
    users = CustomUser.objects.all()
    return render(request, 'cinema/users/users_view.html', {'users': users})


@staff_member_required
def user_change(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == 'POST':
        users = CustomUserForm(request.POST, instance=user)
        if users.is_valid():
            if users.cleaned_data['password'] == users.cleaned_data['password2']:
                users.save()
                return HttpResponseRedirect(reverse_lazy('cinema:users'))
            else:
                return HttpResponse('Пароли не совпадалют')

    users = CustomUserForm(instance=user)
    context = {
        'user': users
    }
    return render(request, 'cinema/users/user_change.html', context)


@staff_member_required
def user_delete(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == 'POST':
        user.delete()
    return HttpResponseRedirect(reverse_lazy('cinema:users'))


@staff_member_required
def delete_template(request):
    if request.headers.get('x-requested-with'):
        print(request.GET)
        try:
            data = request.GET['delete_template']
            print(data)
        except MultiValueDictKeyError:
            print('next Try')
        file = models.HtmlTemplate.objects.get(pk=data)
        file.delete()
        return JsonResponse({}, status=200)


@staff_member_required
def mail_view(request):
    print(request.FILES, request.POST)
    if request.method == 'POST':
        file = request.FILES['file']
        form = HtmlTemplateForm(request.FILES)
        print(form.is_valid(), form.errors)
        if form.is_valid():
            x = models.HtmlTemplate.objects.create(file=file)
            x.save()
            return JsonResponse({}, status=200)


    if request.headers.get('x-requested-with'):
        files = models.HtmlTemplate.objects.order_by('-date')[:5]
        data = []
        for file in files:
            x = {'file_id': file.id,
                 'file_name': file.filename(),
                 }
            data.append(x)

        return JsonResponse({'files': data}, status=200)

    users = CustomUser.objects.order_by('id')
    form_file = HtmlTemplateForm()
    files = models.HtmlTemplate.objects.order_by('-date')[:5]
    context = {
        'form_file': form_file,
        'users': users,
        'files': files,
    }
    return render(request, 'cinema/mail/mail_view.html', context)


@staff_member_required
def send_mail_users(request):
    data = dict(request.POST).pop('emails')
    if request.POST['user_select_all'] == 'true':
        email_list = []
        emails = CustomUser.objects.all().values_list('email')
        for i in emails:
            email_list.append(i[0])
        emails = email_list
    else:
        emails = (data[0].split(' ,'))
        del emails[0]
        emails = set(emails)

    template = models.HtmlTemplate.objects.get(pk=int(request.POST['template']))
    x = template.file.path
    with open(f'{x}', 'r') as file:
        bs = str(BeautifulSoup(file.read(), 'html.parser'))
    for i in emails:
        i.lower()
        letter = mailing.delay(i, template.filename(), bs)
        letter.get()
    return HttpResponse('Done')


@staff_member_required
def statistics_view(request):
    users_registration = CustomUser.objects.filter(is_staff=False, is_superuser=False).count()
    session_list = []
    while len(session_list) < 7:
        day = datetime.date.today() +datetime.timedelta(minutes=5) + datetime.timedelta(days=len(session_list), minutes=5)
        tomorrow = day + datetime.timedelta(days=1, minutes=5)
        session = Session.objects.filter(date__range=(day, tomorrow)).count()
        session_list.append(session)
    movie_data = []
    movie = Film.objects.all()[:7]
    for film in movie:
        movie_data.append(film.session_set.count())
    man = CustomUser.objects.filter(sex='m').count()
    female = CustomUser.objects.filter(sex='f').count()
    context = {'users': users_registration,
               'days_list': session_list,
               'movie_data': movie_data,
               'male':man,
               'female': female,
               }
    return render(request, 'cinema/statictics/statictics.html', context)