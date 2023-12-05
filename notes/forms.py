from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={"class": "form-control mb-5"}),
        }
        labels = {
            'text': 'Write your raw text here:'
        }


# upload file
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        widget=forms.FileInput(attrs={'class': 'btn'})
    )
    title = forms.CharField(
        label="Enter a title for the new summary",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
