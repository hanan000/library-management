from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    SHELF_CHOICES = [
        ('Art', 'Art'),
        ('Technology', 'Technology'),
    ]

    shelf = forms.ChoiceField(choices=SHELF_CHOICES)
    published_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Book
        fields = ['title', 'author', 'shelf', 'published_date']
