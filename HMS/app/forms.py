from django import forms
from .models import *

class RoomsFrom(forms.ModelForm):
    class Meta:
        model=Rooms 
        fields='__all__'
        
class Room_bookFrom(forms.ModelForm):
    class Meta:
        model=Room_book 
        fields='__all__'