from django.forms import ModelForm, ValidationError
from django import forms
from posts.models import *


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'data_published': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            ),
            'data_modified': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            ),
            'text': forms.Textarea(
                attrs={
                    'col': 80,
                    'row': 20
                }
            )
        }

    def clean_data_published(self):
        cleaned_data_published = self.cleaned_data['data_published']

        if cleaned_data_published is None:
            raise ValidationError("Published Date is missing...")

        return cleaned_data_published
