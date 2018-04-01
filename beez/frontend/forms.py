from django import forms


class TerminateHiveForm(forms.Form):
    terminate = forms.HiddenInput(attrs={'value': True})
