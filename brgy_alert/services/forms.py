from django import forms
from .models import ServiceRequest, ServiceRequirement

class ServiceRequestForm(forms.ModelForm):
    def __init__(self, *args, service=None, **kwargs):
        super().__init__(*args, **kwargs)
        if service is not None:
            for req in service.service_requirements.all():
                field_name = f"requirement_{req.id}"
                if req.requirement_type == 'text':
                    self.fields[field_name] = forms.CharField(
                        label=req.label,
                        required=True,
                        widget=forms.TextInput(attrs={'class': 'form-control'})
                    )
                elif req.requirement_type in ['file', 'photo']:
                    self.fields[field_name] = forms.FileField(
                        label=req.label,
                        required=True,
                        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
                    )

    class Meta:
        model = ServiceRequest
        fields = ['reason']
        widgets = {
            'reason': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
        labels = {
            'reason': 'Reason for Request',
        } 