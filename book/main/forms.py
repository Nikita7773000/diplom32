from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Grade


class GradeForm(forms.ModelForm):
    product = forms.ModelMultipleChoiceField(
        queryset=Grade.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Указываем, что это поле необязательно
    )

    class Meta:
        model = Grade
        fields = ['product']  # Указываем, что поле product должно быть в форме


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
