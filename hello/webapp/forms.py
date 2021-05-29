from django import forms
from webapp.models import Album, Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('the_photo', 'signature', 'choice', 'album')

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'description')

class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')


class PhotoDeleteForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Введите название задачи, чтобы удалить её')
