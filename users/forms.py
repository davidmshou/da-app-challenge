from django.forms import ModelForm, TextInput
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            "first_name": TextInput(attrs={"name": "first_name"}),
            "last_name": TextInput(attrs={"name": "last_name"}),
            "email": TextInput(attrs={"name": "email"}),
        }
