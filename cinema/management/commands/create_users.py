import datetime

from django.core.management import BaseCommand
from django.utils.crypto import get_random_string

from users.models import CustomUser


class Command(BaseCommand):
    help = "Create some films for films. python manage.py create_movie 'count' -img 'link' -date 'date' "

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='How many films need to create?')

    def handle(self, *args, **options):
        total = options['total']

        for i in range(total):
            x = CustomUser.objects.create(
                email=f'{get_random_string(10)}@{get_random_string(4)}.com',
                password=f'{get_random_string(8)}',
                phone=f"{get_random_string(10)})",
                first_name=f'{get_random_string(8).title()}',
                last_name=f'{get_random_string(10).title()}',
                date_joined= datetime.date.today(),
                username=f'{get_random_string(10)}'
            )
            x.save()
