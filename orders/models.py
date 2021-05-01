from django.db import models
from houses.models import House


class Order(models.Model):
    house = models.ForeignKey(House, verbose_name="дом", on_delete=models.CASCADE)
    name = models.CharField("имя", max_length=50)
    phone = models.CharField("телефон", max_length=50)
    date = models.DateField("дата", auto_now_add=True)

    class Meta:
        # описательный класс
        verbose_name = "заявка"
        verbose_name_plural = "заявки"
        # сортировка
        ordering = ["date", "name"]

    def __str__(self):
        # houses.object = name in up admin
        return self.name
