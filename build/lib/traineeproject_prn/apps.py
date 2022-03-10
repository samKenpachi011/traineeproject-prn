from tabnanny import verbose
from django.apps import AppConfig as DjangoAppConfig
from django.core.management.color import color_style

style = color_style()

class AppConfig(DjangoAppConfig):
    name = 'traineeproject_prn'
    verbose_name = 'Traineeproject PRN'
    admin_site_name = 'traineeproject_prn_admin'


    # TODO: to include models
    # def ready(self):
    #     from .models import death_report_on_post_save
    #     from .models import subject_offstudy_on_post_save