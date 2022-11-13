from django.forms import ModelForm
from .models import user


class Students_from(ModelForm):
    class Meta:
        model = user
        fields = ['pseudo', 'firstName', 'lastName', 'email', 'phoneNumber', 'birthday']
