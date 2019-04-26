from django.core.mail import EmailMessage
from django.db.models import Count, F, Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from profiles.forms import LoginForm
from profiles.models import Padawan, Jedi
from tests.models import Test


def list_jedi(request):
    if request.POST:
        jedis = Jedi.objects.annotate(count_padawan=Count("padawan_jedi"))\
            .filter(count_padawan__gt=1)
    else:
        jedis = Jedi.objects.select_related().all()
    return render(request, "profiles/list_jedi.html", {"jedis": jedis})


def jedi(request, id):
    count_padawans = Jedi.objects.count_padawan(id)
    if count_padawans >= 3:
        return HttpResponse("Вам уже хватит падаванов")
    padawans = Padawan.objects. \
        filter(planet__order_planet__jedi_order__pk=id, jedi=None). \
        exclude(result_test=None). \
        order_by("-result_test")
    if request.POST:
        mails_padawans = padawans.values_list("email", flat=True)\
            .filter(pk__in=request.POST.getlist('pk'))
        count_new_padawans = mails_padawans.count()
        if count_padawans + count_new_padawans > 3:
            return HttpResponse("Вы выбрали слишком много учеников")
        email = EmailMessage('Jedi academy', 'Вы зачислены в падаваны',
                             to=mails_padawans)
        email.send()
        for pad in padawans:
            pad.jedi_id = id
            pad.save()
        return redirect(reverse("jedi", args=(id, )))
    return render(request,
                  "profiles/profile_jedi.html",
                  {
                      "padawans": padawans
                  })


def padawan(request):
    form = LoginForm()
    if request.POST:
        new_padawan = LoginForm(request.POST)
        if new_padawan.is_valid():
            new_padawan = new_padawan.save()
            request.session["padawan"] = new_padawan.id
            test = Test.objects.only("id")\
                .filter(order__planet__id=new_padawan.planet.id).first()
            if test is None:
                return HttpResponse("Для вашей планеты ещё нет теста")
            return redirect(reverse("test", args=[test.id]))
        return HttpResponse("Данные не верны")
    return render(request, "profiles/authorization.html", {"form": form})


def login(request):
    return render(request, "profiles/login.html")
