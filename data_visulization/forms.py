__author__ = 'fsyed'

from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField()
    verify_password = forms.CharField()
    twitter_account = forms.CharField()

    def clean(self):
        self.validate_password_match()

        super(SignupForm, self).full_clean()

    def create_user(self):
        pass

    def validate_password_match(self):

        password = self.cleaned_data.get('password')
        vpassword = self.cleaned_data.get('verify_password')

        if password != vpassword:
            raise forms.ValidationError('passwords do not match')




class SignupModelForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('is_active', 'last_login', 'date_joined', 'is_superuser', 'is_staff', 'user_permissions',
                'first_name', 'last_name', 'groups')



class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)


