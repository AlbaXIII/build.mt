from .models import Bgcomment
from django import forms

class BgcommentForm(forms.ModelForm):
    class Meta:
        model = Bgcomment
        fields = ('body',)