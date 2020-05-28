from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phone_field import PhoneField

from companyapp.models import Company


class AddCompany(forms.ModelForm):
    rating = forms.DecimalField(min_value=0, max_value=5, decimal_places=1)
    class Meta:
        model = Company
        fields = ('name', 'rating', 'street', 'city', 'website', 'phone', 'category')


class LogForm(forms.Form):
    login = forms.CharField(
        label='Login',
        max_length=50
    )
    password = forms.CharField(
        label='Hasło',
        max_length=30, widget=forms.PasswordInput
    )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label='Imię')
    last_name = forms.CharField(max_length=30, required=False, label='Nazwisko')
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
