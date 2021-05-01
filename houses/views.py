from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from houses.models import House
from orders.forms import OrderForm
from django.http import HttpResponseRedirect


def houses_list(request):
    houses = House.objects.all()  # создаем запрос через ORM, в переменной houses содержаться все дома,
    # которые добавили через админку, эквивалентно SELECT * FROM houses_house ORDER BY name, через модель House
    # получаем все объекты, queryset - набор данных полученных с помощью SQL запроса
    for house in houses:
        print(house.name, house.price, house.date)
    return render(request, "houses/houses_list.html", {"houses": houses})


def house_detail(request, house_id):
    house = get_object_or_404(House, id=house_id)
    form = OrderForm(request.POST or None, initial={"house": house})
    if request.method == "POST":
        if form.is_valid():
            form.save()
            # перезагрузка страницы после сохранения заявки
            return HttpResponseRedirect("{}?sended=True".format(reverse("house", kwargs={"house_id": house_id})))
    return render(request, "houses/house_detail.html",
                  {"house": house, "form": form, "sended": request.GET.get("sended", False)})

