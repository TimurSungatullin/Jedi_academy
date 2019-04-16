from django.db import models

from profiles.models import Planet, Order


class Question(models.Model):
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    question = models.CharField(max_length=200, verbose_name="Вопрос")
    correct_answer = models.BooleanField(verbose_name="Правильный ответ")

    def __str__(self):
        return self.question[:50]


class Test(models.Model):
    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    title = models.CharField(max_length=100, verbose_name="Название")
    order = models.ForeignKey(Order,
                              on_delete=models.PROTECT,
                              verbose_name="Ордер",
                              related_name="test_order")
    questions = models.ManyToManyField(Question,
                                       related_name="test_questions",
                                       verbose_name="Вопросы")

    def __str__(self):
        return self.title
