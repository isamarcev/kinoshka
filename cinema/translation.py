from modeltranslation.translator import register, TranslationOptions
from .models import Cinema, Film, Hall, NewsOrSale, Pages, MainPage


@register(Cinema)
class CinemaTranslationOptions(TranslationOptions):
    fields = ('name', 'describe', 'conveniences')


@register(Film)
class FilmTranslationOptions(TranslationOptions):
    fields = ('title', 'describe')


@register(Hall)
class HallTranslationOptions(TranslationOptions):
    fields = ('title', 'hall_describe')


@register(NewsOrSale)
class NewsOrSaleTranslationOptions(TranslationOptions):
    fields = ('title', 'describe', )

@register(Pages)
class PagesTranslationOptions(TranslationOptions):
    fields = ('title', 'describe', )

@register(MainPage)
class MainPageTranslationOptions(TranslationOptions):
    fields = ('title', 'seo_text')
