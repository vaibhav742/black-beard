from django import forms
from project.models import Gym

class HomeForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    )

    )
    contact_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    )

    )
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    )

    )


    class Meta:
        model = Gym
        fields = ('Name','email','contact_number')
