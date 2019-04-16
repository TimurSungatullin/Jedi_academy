from django.db import models


class Planet(models.Model):
    class Meta:
        verbose_name = "Планета"
        verbose_name_plural = "Планеты"

    title = models.CharField(max_length=100, verbose_name="Название планеты")

    def __str__(self):
        return self.title


class Order(models.Model):
    class Meta:
        verbose_name = "Ордин"
        verbose_name_plural = "Ордин"

    name = models.CharField(max_length=100, verbose_name="Название")
    planet = models.OneToOneField(Planet,
                                  on_delete=models.PROTECT,
                                  verbose_name="Планета",
                                  related_name="order_planet")

    def __str__(self):
        return self.name


class Jedi(models.Model):
    class Meta:
        verbose_name = "Джедай"
        verbose_name_plural = "Джедаи"

    name = models.CharField(max_length=100, verbose_name="Имя")
    order = models.ForeignKey(Order,
                              on_delete=models.PROTECT,
                              verbose_name="Ордин",
                              related_name="jedi_order")

    def __str__(self):
        return self.name


class Padawan(models.Model):
    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"

    name = models.CharField(max_length=100, verbose_name="Имя")
    planet = models.ForeignKey(Planet,
                               on_delete=models.PROTECT,
                               verbose_name="Планета",
                               related_name="padawan_planet")
    age = models.PositiveSmallIntegerField("Возраст")
    email = models.EmailField(verbose_name="E-mail")
    result_test = models.PositiveSmallIntegerField(verbose_name="Результат Теста",
                                                   blank=True,
                                                   null=True)
    jedi = models.ForeignKey(Jedi,
                             on_delete=models.PROTECT,
                             verbose_name="Джедай",
                             blank=True,
                             null=True,
                             related_name="padawan_jedi")

    def __str__(self):
        return self.name
