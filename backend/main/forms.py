from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import *

class EditProfileForm(UserChangeForm):
    
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User

        fields = ('email', 'password')

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data
    
class EditEventForm(forms.ModelForm):
    class Meta:
        model = event
        
        fields = ['name', 'banner', 'email', 'phone', 'description']

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = participant

        fields = ['name', 'email']