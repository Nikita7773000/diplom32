from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Grade


from django import forms
from .models import Grade

class GradeForm(forms.Form):
    product = forms.ModelMultipleChoiceField(
        queryset=Grade.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(GradeForm, self).__init__(*args, **kwargs)
        grades = Grade.objects.all()
        self.fields['product'].initial = grades.filter(is_visible=True)

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
