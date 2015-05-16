from django.forms import ModelForm
from .models import User


# class UserForm(forms.Form):
#     first_name = forms.CharField(label='First name', max_length=100)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
