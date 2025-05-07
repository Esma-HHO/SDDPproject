from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Member

class SignUpForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ['username', 'email', 'telNumber', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Member.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu e-posta zaten kayıtlı.")
        return email


class LoginForm(AuthenticationForm):
    pass
