from django.urls import path
from django.views.generic import TemplateView

from profiles import views

urlpatterns = [
    path('jedi/', views.list_jedi, name="list_jedi"),
    path('jedi/<int:id>', views.jedi, name="jedi"),
    path('padawan/', views.padawan, name="padawan"),
    path('', TemplateView.as_view(template_name="profiles/login.html"), name="login"),
]


