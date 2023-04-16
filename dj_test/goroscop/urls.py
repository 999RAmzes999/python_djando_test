from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFourDigitYearConverter, 'my_float')


urlpatterns = [
    path('', views.index),
    path('type/', views.type),
    path('type/<typing_zodiac>/', views.feaw),
    path('<yyyy:sing_zodiac>/', views.get_yyyy_info),
    path('<int:sing_zodiac>/', views.get_info_about_sing_zodiac_by_number),
    path('<my_float:sing_zodiac>/', views.get_my_float_info),
    path('<str:sing_zodiac>/', views.get_info_about_sing_zodiac, name='goroscop_name'),
]
