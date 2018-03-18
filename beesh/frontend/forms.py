from django import forms


class TransferHiveForm(forms.Form):
    def __init__(self, user, current_apiary_pk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['to_apiary'] = forms.ModelChoiceField(
            queryset=user.apiaries.all().exclude(pk=current_apiary_pk)
        )
