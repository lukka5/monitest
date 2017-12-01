import json
import urllib.parse
import urllib.request

from django import forms
from django.conf import settings

from .models import LoanPetition


class LoanPetitionForm(forms.ModelForm):
    dni = forms.CharField(min_length=7, max_length=10,
                    widget=forms.TextInput(attrs={'type': 'number'}))

    class Meta:
        model = LoanPetition
        fields = ['dni', 'firstname', 'lastname', 'gender', 'email', 'ammount']

    def check_status(self):
        data = {'document_number': self.cleaned_data['dni'],
                'gender': self.cleaned_data['gender'],
                'email': self.cleaned_data['email']}
        params = urllib.parse.urlencode(data)
        url = settings.SCORING_URL + '?' + params
        with urllib.request.urlopen(url) as response:
            try:
                parsed = json.loads(response.read())
            except Exception as e:
                return None, None
        approved, error = parsed.get('approved'), parsed.get('error')
        return approved, error
