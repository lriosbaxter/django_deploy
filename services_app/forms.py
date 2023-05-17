from django import forms
from services_app.models import User


class SignUpUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'age', 'phone_number', 'address']
        widgets = {
            'password': forms.PasswordInput(),
        }