from django import forms
from .models import Function, Collaborator

class FunctionForm(forms.ModelForm):
    class Meta:
        model = Function
        fields = ('name',)


class CollaboratorForm(forms.Form):
    name = forms.CharField(
        max_length=200, 
        required=True, 
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    birth_day = forms.DateField(
        widget=forms.widgets.DateInput(format="%dd/%mm/%YYYY", attrs={'class':'form-control', 'type':'date'}),
        required=True)

    function = forms.ModelChoiceField(
        queryset=Function.objects.all(), 
        widget=forms.Select(attrs={'class':'form-control'}), 
        required=True)
    
    