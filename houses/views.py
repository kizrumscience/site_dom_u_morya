from django.shortcuts import render
from houses.models import House
from django.http import HttpResponse


def houses_list(request):

    houses = House.objects.all()  # создаем запрос через ORM, в переменной houses содержаться все дома,
    # которые добавили через админку, эквивалентно SELECT * FROM houses_house ORDER BY name, через модель House
    # получаем все объекты, queryset - набор данных полученных с помощью SQL запроса
    for house in houses:
        print(house.name, house.price, house.date)
    return render(request, "houses/houses_list.html", {"houses": houses})


def about_house(request, house_name):
    """Опиание дома в отдельной странице"""
    house = House.objects.get(name=house_name)
    output1 = f"<h1><b>{house_name}</b></h1>"
    output2 = f'<h1><br><b>Описание</b></h1> <b>{house_name}</b> продается по цене {house.price}$<br>{house.description}'
    if house.photo:
        return HttpResponse(output1 + f'<img src="{house.photo.url}" alt="{house.name }" width="640" height="480"> <br>'
                            + output2)
    else:
        return HttpResponse(output1 + output2)
