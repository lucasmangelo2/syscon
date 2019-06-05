from django import forms
from .models import Function, Collaborator, Schedule

class FunctionForm(forms.ModelForm):
    class Meta:
        model = Function
        fields = ('name',)

    name = forms.CharField(
        max_length=200, 
        required=True, 
        widget=forms.TextInput(attrs={'class':'form-control'})
    )


class CollaboratorForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        fields = ('name','birth_day', 'function', )

    name = forms.CharField(
        max_length=200, 
        required=True, 
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    birth_day = forms.DateField(
        widget=forms.widgets.DateInput(format="%d/%m/%Y", attrs={'class':'form-control', 'type':'date'}),
        required=True)

    function = forms.ModelChoiceField(
        queryset=Function.objects.all(), 
        widget=forms.Select(attrs={'class':'form-control'}), 
        required=True)
    
    
class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('name','date', 'collaborator', )

    name = forms.CharField(
        max_length=200, 
        required=True, 
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    date = forms.DateField(
        widget=forms.widgets.DateInput(format="%d/%m/%Y", attrs={'class':'form-control', 'type':'datetime'}),
        required=True)

    collaborator = forms.ModelChoiceField(
        queryset=Collaborator.objects.all(), 
        widget=forms.Select(attrs={'class':'form-control'}), 
        required=True)
    
    