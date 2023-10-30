from django.urls import path

from core.web import views

urlpatterns = [
    path('', views.page_view, name='page_view'),
    path('<str:link>/', views.page_view, name='page_view'),
]
