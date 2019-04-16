from django.urls import path

from tests import views

urlpatterns = [
    path('<int:id>', views.view_test, name="test"),
]
