from django import forms
from .models import PhotoAlbum


class UploadFileForm(forms.ModelForm):
    # file = forms.FileField()
    class Meta:
        model = PhotoAlbum
        fields = ['name', 'images']
    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))
    
    
