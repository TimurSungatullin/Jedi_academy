from django import forms

from profiles.models import Padawan


class LoginForm(forms.ModelForm):
    class Meta:
        model = Padawan
        exclude = ["jedi", "result_test"]
