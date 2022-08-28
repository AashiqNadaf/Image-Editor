from django import forms
from django.db.models import fields
from .models import ImageModel


class ImageForm(forms.ModelForm):

    class Meta:
        model = ImageModel
        fields = ['image']