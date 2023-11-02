from django.urls import path

from core.web import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('<str:link>/', views.index_view, name='index_view'),
]
