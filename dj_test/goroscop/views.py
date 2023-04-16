from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from dataclasses import dataclass
# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

type_zodiac = {'Fire': ['aries', 'leo', 'sagittarius'],
               'Earth': ['taurus', 'virgo', 'capricorn'],
               'Air': ['gemini', 'libra', 'aquarius'],
               'Water': ['cancer', 'scorpio', 'pisces']
               }

def index(request):
     #f"<li> <a href='{redirect_path}'>{sing.title()} </a> </li>"
    return render(request, 'goroscop/index.html')

def get_yyyy_info(request, sing_zodiac):
    return HttpResponse(f'Вы передали число из 4 цифр - {sing_zodiac}')

def get_my_float_info(request, sing_zodiac):
    return HttpResponse(f'float number - {sing_zodiac}')

@dataclass
class Person:
    name: str
    age: int

    def __str__(self):
        return f'This is {self.name}'

def get_info_about_sing_zodiac(request, sing_zodiac):
    discription = zodiac_dict.get(sing_zodiac)
    data = {
        'discription_zodiac': discription,
        'sing': sing_zodiac.title(),
        'my_list': [1,2,3],
        'my_tuple': (1, 2, 3),
        'my_int': 1,
        'my_float': 1.2,
        'my_dict': {'name': 'Djon', 'age': 19},
        'my_class': Person('Alies', 18)
    }
    return render(request, "goroscop/info_zodiac.html", context=data)


def get_info_about_sing_zodiac_by_number(request, sing_zodiac):
    zodiac = list(zodiac_dict)
    if sing_zodiac > len(zodiac):
        return HttpResponseNotFound(f'Неизвестный знак зодиака зодиака {sing_zodiac}')
    name_zodiac = zodiac[sing_zodiac - 1]
    redirect_url = reverse('goroscop_name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)

def type(request):
    st_elements = ''
    for st in type_zodiac:
        st_elements += f"<li> <a href='{st}'>{st.title()} </a> </li>"
    response = f"""
        <ol>
            {st_elements}
        </ol>
        """
    return HttpResponse(response)

def feaw(request, typing_zodiac):
    reztip = ''
    tipo = type_zodiac[typing_zodiac]
    for i in tipo:
        ath = reverse('goroscop_name', args=[i])
        reztip += f"<li> <a href='{ath}'>{i.title()} </a> </li>"
        rezpoz = f"""
               <ol>
                   {reztip}
               </ol>
               """
    return HttpResponse(rezpoz)

