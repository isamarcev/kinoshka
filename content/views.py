import datetime
import json

from django.http import JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError

from cinema.models import *
from cinema.forms import SessionForm


def index(request):
    return render(request, 'content/layout/base.html')


def get_date(date):

    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date_list = date.split('-')
    return (str(int(date_list[2])) + ' ' +
            month_list[int(date_list[1]) - 1])


def afisha_view(request):
    start = datetime.date.today()
    end = start + datetime.timedelta(days=1)
    session = Session.objects.filter(date__range=(start, end)).select_related('film', )

    context = {
        'sessions': session,
        'today': get_date(str(datetime.date.today()))

    }
    return render(request, 'content/afisha/afisha.html', context)


def soon_view(request):
    session = Film.objects.filter(date_of_premier=None)
    context = {
        'sessions': session,
    }
    return render(request, 'content/afisha/soon.html', context)


def film_view(request, pk):
    if request.headers.get('x-requested-with'):
        sessions = []
        print(request.GET)
        if request.GET['f2d'] == 'true':
            f2d = True
        else:
            f2d = False
        if request.GET['f3d'] == 'true':
            f3d = True
        else:
            f3d = False
        if request.GET['imax'] == 'true':
            imax = True
        else:
            imax = False
        if all([f2d, f3d, imax]):
            sessions_qs = Session.objects.prefetch_related('hall__cinema', 'film').filter(film=pk)
        else:
            sessions_qs = Session.objects.prefetch_related('hall__cinema', 'film').filter(film=pk)
        if request.GET['date'] == 'false':
            today = datetime.date.today()
            sessions_qs = sessions_qs.filter(date__range=(today, today + datetime.timedelta(days=6)))
        else:
            date = datetime.datetime.strptime((request.GET['date'] + ' 06:00'), "%d-%m-%Y %H:%M")
            date_range = (date, date + datetime.timedelta(days=1))
            sessions_qs = sessions_qs.filter(date__range=date_range)
        if request.GET['cinema_id'] != 'false':
            sessions_qs = sessions_qs.filter(hall__cinema_id=request.GET['cinema_id'])
        for session in sessions_qs:
            d = session.date.strftime("%d/%B/%Y")
            t = session.date.strftime("%H:%M")
            x = {'session_date': d,
                 'session_time': t,
                 'hall_id': session.hall.id,
                 'hall_name': session.hall.title,
                 'price': session.price,
                 'session': session.id,
                 'film_name': session.film.title}
            sessions.append(x)
        return JsonResponse({'sessions': sessions}, status=200)


    film = Film.objects.prefetch_related('session_set__hall__cinema', 'pictures__photo_set').get(pk=pk)
    cinema = Cinema.objects.all()

    count = range(1, len(film.pictures.photo_set.all()))
    slider_count = []
    for i in count:
        slider_count.append(i)
    print(slider_count)
    context = {
        'film': film,
        'cinema': cinema,
        'today': [datetime.date.today(), datetime.date.today() + datetime.timedelta(days=1),
                  datetime.date.today() + datetime.timedelta(days=2),
                  datetime.date.today() + datetime.timedelta(days=3),
                  datetime.date.today() + datetime.timedelta(days=4),
                  datetime.date.today() + datetime.timedelta(days=5),
                  datetime.date.today() + datetime.timedelta(days=6),
                  datetime.date.today() + datetime.timedelta(days=7),
                  ],
        'slider_count': slider_count,
    }
    return render(request, 'content/film/film_view.html', context)


def shedule_view_cinema_up(request):
    if request.headers.get('x-requested-with'):
        x = dict(request.GET)
        try:
            date = x['date'][0]
        except:
            date = datetime.date.today()
        if (x['cinema_id'][0]) != 'false':
            cinema_id = int(x['cinema_id'][0])
            session = Session.objects.order_by('date').prefetch_related('hall__cinema', 'film'). \
                filter(hall__cinema=cinema_id, date__range=(date, date + datetime.timedelta(days=1)))
            hall = Hall.objects.filter(cinema_id=cinema_id)
        else:
            session = Session.objects.order_by('date').prefetch_related('hall__cinema', 'film'). \
                filter(date__range=(date, date + datetime.timedelta(days=1)))
        sessions = []
        halls = []
        for i in session:
            d = i.date.strftime("%d/%B/%Y")
            t = i.date.strftime("%H:%M")
            x = {'cinema': i.hall.cinema_id,
                'film_name': i.film.title,
                'film_id': i.film.id,
                'session_date': d,
                'session_time': t,
                'hall_id': i.hall.id,
                'hall_name': i.hall.title,
                 'price': i.price}
            sessions.append(x)
        try:
            for i in hall:
                x = {'hall_name': i.title,
                     'hall_id': i.id,
                    }
                halls.append(x)
        except:
            pass
        return JsonResponse({'halls': halls, 'session': sessions}, status=200)


def shedule_view(request):
    if request.headers.get('x-requested-with'):
        x = dict(request.GET)
        try:
            date = datetime.datetime.strptime(str(x['date'][0]), "%d-%m-%Y")
            end = date + datetime.timedelta(days=1)
        except:
            date = datetime.date.today()
            end = date + datetime.timedelta(days=1)

        if x['2d'][0] == 'true':
            f2d = True
        else:
            f2d = False
        if x['3d'][0] == 'true':
            f3d = True
        else:
            f3d = False
        if x['imax'][0] == 'true':
            imax = True
        else:
            imax = False
        if all([f2d, f3d, imax]):
            session = Session.objects.order_by('date').prefetch_related('hall', 'film'). \
            filter(date__range=(date, end))
        else:
            session = Session.objects.order_by('date').prefetch_related('hall', 'film'). \
                    filter(date__range=(date, end), film__IMAX=imax,
                            film__f2d=f2d, film__f3d=f3d)
        sessions = []
        try:
            session = session.filter(film_id=int(x['film_id'][0]))
        except:
            pass
        if x['hall_id'][0] != 'false':
            session = session.filter(hall_id=(x['hall_id'][0]))
        for i in session:
                d = i.date.strftime("%d/%B/%Y")
                t = i.date.strftime("%H:%M")
                x = {'cinema': i.hall.cinema_id,
                    'film_name': i.film.title,
                    'film_id': i.film.id,
                    'session_id': i.id,
                    'session_date': d,
                    'session_time': t,
                    'hall_id': i.hall.id,
                    'hall_name': i.hall.title,
                    'price': i.price}
                sessions.append(x)
        return JsonResponse({'session': sessions}, status=200)

    cinemas = Cinema.objects.all()
    films = Film.objects.all()
    context = {
        'cinemas': cinemas,
        'films': films,
        'today': [datetime.date.today(), datetime.date.today() + datetime.timedelta(days=1),
                  datetime.date.today() + datetime.timedelta(days=2),
                  datetime.date.today() + datetime.timedelta(days=3),
                  datetime.date.today() + datetime.timedelta(days=4),
                  datetime.date.today() + datetime.timedelta(days=5),
                  datetime.date.today() + datetime.timedelta(days=6),
                  datetime.date.today() + datetime.timedelta(days=7),
                  ]
    }
    return render(request, 'content/afisha/shedule.html', context)


def bought_ticket(request):
    session = Session.objects.filter(pk=request.POST['session']).first()
    map = session.place
    try:
        data = request.POST['place']
    except MultiValueDictKeyError:
        return None
    places = data.split(',')
    tickets = 'В Вашем билете: '
    del places[-1]
    for i in places:
        rowseat = i.split(':')
        map[rowseat[0]][rowseat[1]]['bought'] = True
        tickets += f'Ряд {rowseat[0]} Место {rowseat[1]} .'
    session.save()
    user = request.user.id
    ticket = Ticket.objects.create(user_id=user, session_id=session.id, places=tickets)
    ticket.save()
    return JsonResponse({'fasdf': True}, status=200)


def buy_tickets(request, pk):
    session = Session.objects.filter(pk=pk).prefetch_related('hall', 'film').first()
    hall = session.hall
    film = session.film
    if request.headers.get('x-requested-with'):
        if not session.place:
            session.place = session.hall.places
            session.save()
            print('save')
        x = session.place
        return JsonResponse(x, status=200)
    x = session
    context = {'hall': hall, 'film': film, 'session': session}
    return render(request, 'content/film/tickets.html', context)


def cinemas_view(request):
    cinemas = Cinema.objects.all()
    context = {
        'cinemas': cinemas
    }
    return render(request, 'content/cinema/cinema_list.html', context)


def cinema_view(request, pk):

    cinema = Cinema.objects.prefetch_related('hall_set__session_set', 'pictures__photo_set').get(pk=pk)
    context = {
        'cinema': cinema,
    }
    return render(request, 'content/cinema/cinema_view.html', context)


def hall_view(request, pk):
    hall = Hall.objects.prefetch_related('session_set', 'pictures__photo_set').get(pk=pk)
    context = {
        'hall': hall,
    }
    return render(request, 'content/hall/hall_view.html', context)


def sales_view(request):
    sales = NewsOrSale.objects.filter(news_or_sale='sale').select_related('pictures').prefetch_related('pictures__photo_set')
    banner = BannerBox.objects.filter(news_or_main='news').prefetch_related('banner_set').first()
    context = {
        'sales': sales,
        'banner': banner,
    }
    return render(request, 'content/sale/sale_list.html', context)


def sale_view(request, pk):
    sales = NewsOrSale.objects.select_related('pictures').prefetch_related('pictures__photo_set').get(pk=pk)
    print(sales)
    cinemas = Cinema.objects.all()
    banner = BannerBox.objects.filter(news_or_main='news').prefetch_related('banner_set').first()
    context = {
        'sales': sales,
        'cinemas': cinemas,
        'banner': banner,
    }
    return render(request, 'content/sale/sale_view.html', context)


def news_view(request):
    news = NewsOrSale.objects.filter(news_or_sale='news').select_related('pictures').prefetch_related('pictures__photo_set')
    banner = BannerBox.objects.filter(news_or_main='news').prefetch_related('banner_set').first()
    context = {
        'sales': news,
        'banner': banner,
    }
    return render(request, 'content/news/news_list.html', context)


def new_view(request, pk):
    new = NewsOrSale.objects.select_related('pictures').prefetch_related('pictures__photo_set').get(pk=pk)
    cinemas = Cinema.objects.all()
    banner = BannerBox.objects.filter(news_or_main='news').prefetch_related('banner_set').first()
    context = {
        'sales': new,
        'cinemas': cinemas,
        'banner': banner,
    }
    return render(request, 'content/news/new_view.html', context)


def coffee_bar(request):
    bar = Pages.objects.filter(title__endswith='Бар').select_related('pictures').prefetch_related('pictures__photo_set').first()
    context = {
        'bar': bar,
    }
    return render(request, 'content/pages/coffee_bar.html', context)


def vip_hall(request):
    vip = Pages.objects.filter(title__startswith='Vip').select_related('pictures').\
        prefetch_related('pictures__photo_set').first()
    context = {
        'vip': vip,
    }
    return render(request, 'content/pages/vip-hall.html', context)



def adversting_view(request):
    adv = Pages.objects.filter(title__startswith='Реклама').select_related('pictures').\
        prefetch_related('pictures__photo_set').first()
    context = {
        'vip': adv,
    }
    return render(request, 'content/pages/adv.html', context)


def mobile_view(request):
    mob = Pages.objects.filter(title__startswith='Моб').select_related('pictures').\
        prefetch_related('pictures__photo_set').first()
    context = {
        'vip': mob,
    }
    return render(request, 'content/pages/mobile.html', context)


def contacts_view(request):
    contacts = Contacts.objects.all()
    context = {
        'contacts': contacts,
    }
    return render(request, 'content/pages/contacts.html', context)


def main_page(request):
    mainPage = MainPage.objects.first()
    backgroundbanner = BackgroundBanner.objects.first()
    banners = BannerBox.objects.all().prefetch_related('banner_set')
    start = datetime.date.today()
    end = start + datetime.timedelta(days=1)
    session = Session.objects.filter(date__range=(start, end)).select_related('film',)

    context = {
        'main_page': mainPage,
        'banners': banners,
        'sessions': session,
        'backgroundbanner': backgroundbanner,
        'today': get_date(str(datetime.date.today()))

    }
    return render(request, 'content/pages/main_page.html', context)