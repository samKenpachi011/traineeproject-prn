import imp
from django import forms
from ..models import SubjectOffStudy
from edc_form_validators import FormValidatorMixin


# TODO: Add in validators

class SubjectOffStudyForm(forms.ModelForm):
    
    # subject_identifier = forms.CharField(
    #     label='Subject Identifier',
    #     widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = SubjectOffStudy
        fields = '__all__'