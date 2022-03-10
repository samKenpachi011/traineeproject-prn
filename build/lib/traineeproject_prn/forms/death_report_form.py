from dataclasses import fields
from pyexpat import model
from django import forms
from ..models import DeathReport


class DeathReportForm(forms.ModelForm):

    class Meta:
        model = DeathReport
        fields = '__all__'