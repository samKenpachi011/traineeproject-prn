from statistics import mode
from tabnanny import verbose
from django.apps import apps as django_apps
from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_action_item.model_mixins import ActionModelMixin
from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.utils import get_utcnow
from edc_identifier.managers import SubjectIdentifierManager
from edc_protocol.validators import (
    date_not_before_study_start, datetime_not_before_study_start)


from ..choices import OFF_STUDY_REASON

# TODO: add validations
class SubjectOffStudy(ActionModelMixin,BaseUuidModel):

    action_name = 'submit-subject-offstudy'

    tracking_identifier_prefix = 'SO'

    subject_identifier = models.CharField(
        max_length=50,
        unique=True)

    offstudy_date = models.DateField(
        verbose_name='Offstudy date',
        validators=[date_not_before_study_start, datetime_not_before_study_start],
        null=True,
        default=get_utcnow,)

    report_datetime = models.DateTimeField(
        verbose_name='Report datetime',
        validators=[date_not_before_study_start, datetime_not_before_study_start],
        null=True,
        default=get_utcnow,)

    reason = models.CharField(
        verbose_name='Reason for exit',
        max_length=50,
        choices=OFF_STUDY_REASON,
        null=True,)

    reason_other = OtherCharField()

    comment = models.TextField(
        max_length=250,
        verbose_name='Comment',
        blank=True,
        null=True)

    def natural_key(self):
        return (self.subject_identifier)
    natural_key.dependencies = ['sites.Site']

    def save(self, *args, **kwargs):
        self.consent_version = None
        super().save(*args, **kwargs)  

    objects = SubjectIdentifierManager()
    history = HistoricalRecords()

    class Meta:
        app_label = 'traineeproject_prn'
        verbose_name = 'Traineeproject PRN'
        verbose_name_plural = 'Subject Off Study'


