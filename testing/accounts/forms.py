from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account
from django.contrib.auth import authenticate


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("email", "username", "first_name", "last_name", "password1", "password2")


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Incorrect Login')


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'username')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" already exists.' % email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" already exists.' % username)

    def clean_password(self):
        if self.is_valid():
            password = self.cleaned_data['password']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(password=password)
            except Account.DoesNotExist:
                return password
            raise forms.ValidationError('Username "%s" already exists.' % password)




