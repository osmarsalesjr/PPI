from django.forms import *
from django import forms
from library.models import *


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'tittle', 'birth_date']
        widgets = {
            'birth_date': DateInput(
                attrs={
                    'type': 'date',
                }
            )
        }


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'authors': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields["authors"].queryset = Author.objects.filter(active=True)
