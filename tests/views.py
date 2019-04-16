from django.http import HttpResponse
from django.shortcuts import render

from profiles.models import Padawan
from tests.models import Test


def view_test(request, id):
    if "padawan" not in request.session:
        return HttpResponse("Вы не падаван")
    test = Test.objects.prefetch_related("questions").get(pk=id)
    if request.POST:
        result = 0
        questions = test.questions.all()
        for question in questions:
            if (question.correct_answer == (str(question.pk) in request.POST)):
                result += 1
        result = result / questions.count() * 100
        padawan = Padawan.objects.get(pk=request.session["padawan"])
        padawan.result_test = result
        padawan.save()
        return HttpResponse("Ваш резуьтат %d. Ожидайте письма от ордера джедаев" % result)
    return render(request, "tests/test.html", {"test": test})
