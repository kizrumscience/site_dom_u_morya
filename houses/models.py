from django.db import models


class House(models.Model):
    name = models.CharField("название", max_length=50)
    price = models.IntegerField("цена")
    description = models.TextField("описание")
    date = models.DateField("дата", default='2020-01-01')
    photo = models.ImageField("фотография", upload_to="houses/photos", default="", blank=True)

    class Meta:
        # описательный класс
        verbose_name = "дом"
        verbose_name_plural = "дома"
        # сортировка
        ordering = ["name", "price"]

    def __str__(self):
        # houses.object = name in up admin
        return self.name.upper()
