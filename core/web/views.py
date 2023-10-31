from django.shortcuts import get_object_or_404, render

from .models import Page


def page_view(request, link=''):
    page = get_object_or_404(Page, link=link)

    lang = request.COOKIES.get('lang', 'ukr')

    response = render(request, 'page.html', {'page': page, 'lang': lang})
    if 'lang' not in request.COOKIES:
        response.set_cookie('lang', 'ukr')

    return response
