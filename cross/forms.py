from django import forms
from . import models



class SneakersForm(forms.ModelForm):
    class Meta:
        model = models.Sneakers
        fields = '__all__'







