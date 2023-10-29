from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Page


def page_view(request, link):
    page = get_object_or_404(Page, link=link)

    content = f"""
    <h1>{page.name_ukr}</h1>
    <div>{page.content_ukr}</div>

    <h1>{page.name_eng}</h1>
    <div>{page.content_eng}</div>
    """

    return HttpResponse(content)
