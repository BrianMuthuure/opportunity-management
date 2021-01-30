from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from main.models import Opportunity, Account


class ExtendedUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is already taken")
        return username


class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = '__all__'


class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'