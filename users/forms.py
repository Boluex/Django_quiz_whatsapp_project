from django.forms import ModelForm
from.models import profile
from django.contrib.auth.models import User


class user_form(ModelForm):
    class Meta:
        model=User
        fields=['username','email']
        
        
