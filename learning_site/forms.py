__author__ = 'om'
from django import forms
from django.core import validators

class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify = forms.EmailField(label="Verify your email address")
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput,
                               label="Leave it empty.", validators=[validators.MaxLengthValidator(0)])

    #def clean_honeypot(self):
        #honeypot = self.cleaned_data['honeypot']
        #if len(honeypot):
            #raise forms.ValidationError("Honeypot should left empty.")
        #return honeypot

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('verify')
        if email != verify:
            raise forms.ValidationError('both email should same!')