from django.shortcuts import render
from houses.models import House


def houses_list(request):

    houses = House.objects.all() # создаем запрос через ORM, в переменной houses содержаться все дома,
    # которые добавили через админку, эквивалентно SELECT * FROM houses_house ORDER BY name, через модель House
    # получаем все объекты, queryset - набор данных полученных с помощью SQL запроса
    for house in houses:
        print(house.name, house.price)
    return render(request, "houses/houses_list.html", {"houses": houses})
