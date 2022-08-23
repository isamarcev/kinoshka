import datetime

from django.core.management import BaseCommand
from django.utils.crypto import get_random_string

from cinema.models import Film, Gallery, Seo


class Command(BaseCommand):
    help = "Create some films for films. python manage.py create_movie 'count' -img 'link' -date 'date' "

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='How many films need to create?')
        parser.add_argument('-img', '--image', type=str, help='link for img logo in the root MEDIA')
        parser.add_argument('-date', '--date_premier', type=str, help='link for img logo in the root MEDIA')

    def handle(self, *args, **options):
        total = options['total']
        img = options['image']
        if options['date_premier']:
            date = options['date_premier']
        else:
            date = datetime.date.today()

        for i in range(total):
            x = Film.objects.create(
                title=f'{get_random_string(10)} {get_random_string(10)}',
                describe=f'{get_random_string(200)}',
                pictures=Gallery.objects.create(title=f'{get_random_string(10)} film'),
                seo=Seo.objects.create(title=f'{get_random_string(10)} random'),
                logo=img,
                date_of_premier=date,
            )
            x.save()
