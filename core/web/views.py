from django.shortcuts import get_object_or_404, render

from .models import Page


def page_view(request, link=''):
    page = get_object_or_404(Page, link=link)
    return render(request, 'page.html', {'page': page})
