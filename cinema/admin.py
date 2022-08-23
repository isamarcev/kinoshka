from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Cinema, Film, Hall, Session, Gallery, Photo, Seo, BackgroundBanner, BannerBox, Banner, MainPage, \
    Contacts, NewsOrSale, Pages, Ticket, HtmlTemplate


@admin.register(Cinema)
class CinemaAdmin(TranslationAdmin):
    pass


@admin.register(Film)
class FilmAdmin(TranslationAdmin):
    pass


@admin.register(Hall)
class HallAdmin(TranslationAdmin):
    pass


@admin.register(NewsOrSale)
class NewsOrSaleAdmin(TranslationAdmin):
    pass


@admin.register(Pages)
class PagesAdmin(TranslationAdmin):
    pass

@admin.register(MainPage)
class MainPageAdmin(TranslationAdmin):
    pass


admin.site.register(HtmlTemplate)

admin.site.register(Session)
admin.site.register(Gallery)
admin.site.register(Photo)
admin.site.register(Seo)
admin.site.register(BackgroundBanner)
admin.site.register(BannerBox)
admin.site.register(Banner)
admin.site.register(Contacts)
admin.site.register(Ticket)

# Register your models here.
