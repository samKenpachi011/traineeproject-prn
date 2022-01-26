from django.apps import apps as django_apps
from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.utils import get_utcnow


class SubjectOffStudy():
    pass