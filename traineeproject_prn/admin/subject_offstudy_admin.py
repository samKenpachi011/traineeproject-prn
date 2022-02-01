from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from ..admin_site import traineeproject_prn_admin
from ..models import SubjectOffStudy
from ..forms import SubjectOffStudyForm
from ..admin_site import traineeproject_prn_admin
from .modeladmin_mixins import ModelAdminMixin

@admin.register(SubjectOffStudy, site=traineeproject_prn_admin)
class SubjectOffStudyAdmin(ModelAdminMixin,admin.ModelAdmin):
    
    form = SubjectOffStudyForm
    fieldsets = (
    (None, {
        'fields': [
            'subject_identifier',
            'report_datetime',
            'offstudy_date',
            'completed_study',
            'reason',
            'reason_other',
            'death_date',
            'comment']}
        ), audit_fieldset_tuple)

    radio_fields = {
        'completed_study': admin.VERTICAL,
        'reason': admin.VERTICAL,
    }

    search_fields = ('subject_identifier', )

    list_display = ('subject_identifier', 'offstudy_date', )    