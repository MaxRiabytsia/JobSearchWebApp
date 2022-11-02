from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 100%; height: 20%'}))

    class Meta:
        model = Job
        exclude = ('date_added', 'creator')
