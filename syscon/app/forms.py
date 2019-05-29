from django import forms
from .models import Function, Collaborator

class FunctionForm(forms.ModelForm):

    class Meta:
        model = Function
        fields = ('name',)


class CollaboratorForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        fields = ('name','birth_day','function')

    ''' model = Collaborator
    name = forms.CharField(max_length=200, required=True)
    birth_day = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"),required=True)
    function = forms.ModelChoiceField(queryset=Function.objects.all(), widget=forms.Select, required=True)
    '''
    