__author__ = 'akash'


from django import forms
from models import Books

class BookForm(forms.ModelForm):

    class Meta:
        model=Books
        fields=('book_name','author_name','description','thumbnail')
