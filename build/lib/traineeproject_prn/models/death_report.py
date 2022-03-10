from django.db import models

from edc_action_item.model_mixins import ActionModelMixin
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO

from edc_base.model_validators import date_not_future
from edc_base.model_validators import datetime_not_future
from edc_protocol.validators import datetime_not_before_study_start

from ..action_items import DEATH_REPORT_ACTION
from ..choices import DEATH_INFO_SOURCE, PLACE_OF_DEATH, FACILITY
from ..choices import MED_RESPONSIBILITY, HOSPITALIZATION_REASON, CAUSE_OF_DEATH_CAT

class DeathReport(SiteModelMixin, ActionModelMixin, BaseUuidModel):
    action_name = DEATH_REPORT_ACTION

    tracking_identifier_prefix = 'DR'

    report_datetime = models.DateTimeField(
        verbose_name='Report Date',
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use'
                    ' the date/time this information was reported.'))

    death_date = models.DateField(
        validators=[date_not_future],
        verbose_name='Date of Death:')

    cause_of_death = models.CharField(
        verbose_name='What is the primary source of cause of death '
                        'information?',
        max_length=50,
        choices=CAUSE_OF_DEATH_CAT,)
    
    source_of_cause = models.CharField(
        max_length=50,
        choices=DEATH_INFO_SOURCE,
        verbose_name=('What was the source of information about participant'
                        'death?'
                        )) 

    place_of_death = models.CharField(
        verbose_name=('Name the place where the patient died?'),
        choices=PLACE_OF_DEATH,
        max_length=20,)

    facility_patient_died = models.CharField(
        verbose_name=('Name of the facility where the patient died?'),
        choices=FACILITY,
        max_length=50,
        blank=True,
        null=True,)                    

    medical_responsibility = models.CharField(
        choices=MED_RESPONSIBILITY,
        max_length=50,
        verbose_name=('Who was responsible for primary medical care of the '
                      'participant during the month prior to death?'))

    reason_participant_hospitalized = models.CharField(
        max_length=65,
        choices=HOSPITALIZATION_REASON,
        verbose_name='Why was the participant hospitalised before death?',
        blank=True,
        null=True)


    comments = models.TextField(
        verbose_name='Comments',
        blank=True,
        null=True)

    class Meta:
        app_label = 'traineeproject_prn'
        verbose_name = 'Death Report'
        verbose_name_plural = 'Death Report'




