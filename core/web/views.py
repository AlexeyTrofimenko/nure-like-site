from django.shortcuts import get_object_or_404, render

from .models import Page


def index_view(request, link=''):
    page = get_object_or_404(Page, link=link)
    lang = request.COOKIES.get('lang', 'ukr')
    nav_pages = Page.objects.exclude(link='')

    response = render(request, 'index.html', {'page': page, 'lang': lang, 'nav_pages': nav_pages})
    if 'lang' not in request.COOKIES:
        response.set_cookie('lang', 'ukr')

    return response
