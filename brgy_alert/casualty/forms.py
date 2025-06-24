from django import forms
from .models import CasualtyReport

class CasualtyReportForm(forms.ModelForm):
    class Meta:
        model = CasualtyReport
        exclude = ['reporter', 'status', 'timestamp'] 