from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFourDigitYearConverter, 'my_float')


urlpatterns = [
    path('', views.index, name='goroscop_index'),
    path('type/', views.type, name='goroscop_type'),
    path('type/<typing_zodiac>/', views.feaw, name='goroscop_feaw'),
    path('<int:sing_zodiac>/', views.get_info_about_sing_zodiac_by_number),
    path('<str:sing_zodiac>/', views.get_info_about_sing_zodiac, name='goroscop_name'),
]
