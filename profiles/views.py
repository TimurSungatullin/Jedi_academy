from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from profiles.forms import LoginForm
from profiles.models import Padawan, Jedi
from tests.models import Test


def list_jedi(request):
    jedis = Jedi.objects.all()
    return render(request, "profiles/list_jedi.html", {"jedis": jedis})


def jedi(request, id):
    jedi = Jedi.objects.get(id=id)
    padawans = Padawan.objects.filter(planet=jedi.order.planet.pk, jedi=None).order_by("-result_test")
    if request.POST:
        for pad in padawans:
            if str(pad.pk) in request.POST:
                pad.jedi = jedi
                pad.save()
        return HttpResponse("Падаваны зачислены!")
    return render(request, "profiles/profile_jedi.html", {"padawans": padawans})


def padawan(request):
    form = LoginForm()
    if request.POST:
        new_padawan = LoginForm(request.POST)
        new_padawan = new_padawan.save()
        request.session["padawan"] = new_padawan.id
        test = Test.objects.only("id").filter(order__planet__id=new_padawan.planet.id).first()
        if test is None:
            return HttpResponse("Для вашей планеты ещё нет теста")
        return redirect(reverse("test", args=[test.id]))
    return render(request, "profiles/authorization.html", {"form": form})


def login(request):
    return render(request, "profiles/login.html")
