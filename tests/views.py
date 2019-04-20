from django.db.models import Count, F, Q
from django.http import HttpResponse
from django.shortcuts import render

from profiles.models import Padawan
from tests.models import Test


def view_test(request, id):
    if "padawan" not in request.session:
        return HttpResponse("Вы не падаван")
    test = Test.objects.prefetch_related("questions").get(pk=id)
    if request.POST:
        correct_answer = Q(correct_answer=True)
        selected_answer = Q(pk__in=request.POST.getlist('pk'))
        correct_questions = (correct_answer & selected_answer) | (~correct_answer & ~ selected_answer)
        questions = test.questions.aggregate(all_questions=Count('pk'),
                                             correct_questions=Count('pk', filter=correct_questions))
        result = questions['correct_questions'] / questions['all_questions'] * 100
        padawan = Padawan.objects.get(pk=request.session["padawan"])
        padawan.result_test = result
        padawan.save()
        return HttpResponse("Ваш резуьтат %d. Ожидайте письма от ордера джедаев" % result)
    return render(request, "tests/test.html", {"test": test})
