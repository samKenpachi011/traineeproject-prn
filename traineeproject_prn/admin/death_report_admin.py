import imp
from django.contrib import admin
from django.db import models
from ..admin_site import traineeproject_prn_admin
from edc_model_admin import audit_fieldset_tuple
from .modeladmin_mixins import ModelAdminMixin
from ..models import DeathReport
from ..forms import DeathReportForm

@admin.register(DeathReport, site=traineeproject_prn_admin)
class DeathReportAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = DeathReportForm

    search_fields = ('subject_identifier',)

    fieldsets = ((None,{
        'fields':[
            'subject_identifier',
            'report_datetime',
            'death_date',
            'cause_of_death',
            'source_of_cause',
            'place_of_death',
            'facility_patient_died',
            'medical_responsibility',
            'reason_participant_hospitalized',
            'comments',
        ]
    }),audit_fieldset_tuple)

    radio_fields = {
        'cause_of_death': admin.VERTICAL,
        'medical_responsibility': admin.VERTICAL,
        'place_of_death': admin.VERTICAL,
        'facility_patient_died': admin.VERTICAL,}




