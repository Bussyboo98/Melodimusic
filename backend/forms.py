from django import forms
from frontend.models import *
from django.core import validators



    
class FilterForm(forms.ModelForm):
     
    ONE = "Ajah"
    TWO = "Agege"
    THREE = "Ikeja"
    FOUR = "Lekki Phase 1"
    FIVE = "Lekki Phase 2"
    SIX = "Ikoyi"
    SEVEN = "Oshodi"
    EIGHT = "Magodo"
    NINE = "Victoria Island"
    TEN = "Oniru VI"
    ONE1 = "Mowe"
    TWO2 = "Ikorodu"
    THREE3 = "Festac"
    FOUR4 = "Ojodu"
    FIVE5 = "Banana Island"
    SIX6 = "Maryland"
    SEVEN7 = "Ogba"
    EIGHT8 = "Barracks" 
    CHOOSE = ""

    LOCATION= [
          (ONE, "Ajah"),
        (TWO, "Agege"),
        (THREE, "Ikeja"),
        (FOUR, "Lekki Phase 1"),
        (FIVE, "Lekki Phase 2"),
        (SIX, "Ikoyi"),
        (SEVEN, "Oshodi"),
        (EIGHT, "Magodo"),
        (NINE, "Victoria Island"),
        (TEN, "Oniru VI"),
        (ONE1, "Mowe"),
       (TWO2, "Ikorodu"),
       (THREE3, "Festac"),
        (FOUR4, "Ojodu"),
       (FIVE5, "Banana Island"),
       (SIX6, "Maryland"),
       (SEVEN7, "Ogba"),
       (EIGHT8, "Barracks"), 
       (CHOOSE, 'Location')
    ]

    song = forms.CharField(required=False, label='Song*', widget=forms.Select(choices=LOCATION,
        attrs={'class': 'form-control', 'placeholder': 'Song'}))

    class Meta():
        fields = ['song']
        model = Artiste
    