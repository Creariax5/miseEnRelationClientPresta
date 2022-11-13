from django.forms import ModelForm
from .models import Students


class Students_from(ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'email']
