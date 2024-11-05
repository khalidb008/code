from django import forms
from .models import climate

class climateform(forms.ModelForm):
    class Meta:
        model = climate
        fields = ('location', 'temperature', 'flood', 'drought', 'social_disruption', 'indigenous_forecasting')