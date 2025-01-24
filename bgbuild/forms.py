from .models import Bgcomment, Bgreply
from django import forms

class BgcommentForm(forms.ModelForm):
    class Meta:
        model = Bgcomment
        fields = ('body',)

class BgreplyForm(forms.ModelForm):
    class Meta:
        model = Bgreply
        fields = ('body',)