from django.core.mail import send_mail, EmailMessage
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from profiles.forms import LoginForm
from profiles.models import Padawan, Jedi
from tests.models import Test


def list_jedi(request):
    if request.POST:
        jedis = Jedi.objects.annotate(count_padawan=Count("padawan_jedi")).filter(count_padawan__gt=1)
    else:
        jedis = Jedi.objects.select_related().all()
    return render(request, "profiles/list_jedi.html", {"jedis": jedis})


def jedi(request, id):
    jedi = Jedi.objects.get(id=id)
    if jedi.count_padawan() >= 3:
        return HttpResponse("Вам уже хватит падаванов")
    padawans = Padawan.objects.\
        filter(planet=jedi.order.planet.pk, jedi=None).\
        exclude(result_test=None).\
        order_by("-result_test")
    if request.POST:
        mails_padawans = []
        for pad in padawans:
            if str(pad.pk) in request.POST:
                mails_padawans.append(pad.email)
                try:
                    email.send()
                    pad.jedi = jedi
                    pad.save()
                except SMTPAuthenticationError:
                    continue
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
