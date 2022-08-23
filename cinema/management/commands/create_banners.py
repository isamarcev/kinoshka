from django.core.management import BaseCommand


from cinema.models import Banner, BackgroundBanner, BannerBox


class Command(BaseCommand):
    help = "Create banners: main, news, background"

    def handle(self, *args, **options):
        main_banner = BannerBox.objects.create(title='На главной верх')
        news_banner = BannerBox.objects.create(title='На главной верх', news_or_main='news')
        main_banner.save()
        news_banner.save()
        background_banner = BackgroundBanner.objects.create(type='Фото на фоне', title="баннер на заднем фоне")
        background_banner.save()
