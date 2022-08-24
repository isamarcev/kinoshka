import datetime
import math

from django.core.management import BaseCommand
import random
import time


from cinema.models import Film, Hall, Session


def get_random(start, end, format):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    delta = (etime - stime)/60/60
    return stime, etime, delta

print(get_random('7/2/2022 8:00 AM', '7/2/2022 11:00 PM', '%m/%d/%Y %I:%M %p'))





def strTimeProp(start, end, format, prop):

            stime = time.mktime(time.strptime(start, format))
            etime = time.mktime(time.strptime(end, format))

            ptime = stime + prop * (etime - stime)

            return time.strftime(format, time.localtime(ptime))

def randomDate(start, end, prop):
        return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)

print(randomDate("7/2/2022 8:00 AM", "7/2/2022 11:00 PM", random.random()))


def random_item(model, max_id=None):
    x = model.objects.filter(date_of_premier=False).order_by('?').first()
    return x

print(random_item(Film))

class Command(BaseCommand):
    help = "Create some session for films. python manage.py create_session '--date'(today)/%Y-%m-%d "

    def add_arguments(self, parser):
        parser.add_argument('date', type=str, help='%Y-%m-%d')

    def handle(self, *args, **options):
        if options['date']:
            date = options['date']
        else:
            date = datetime.date.today()
        count = 1
        time = ['8:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00', ]
        day = [f'{date} {x}' for x in time]
        halls = Hall.objects.all()
        for c in range(count):
            for halla in halls:
                for i in day:
                    session = Session.objects.create(
                         name=f'{i} {halla.title} session',
                         date=i,
                         film=random_item(Film),
                         price=random.randint(100, 200),
                         hall=halla
                    )
                    session.save()


