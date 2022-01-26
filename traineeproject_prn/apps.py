from tabnanny import verbose
from django.apps import AppConfig as DjangoAppConfig

class AppConfig(DjangoAppConfig):
    name = 'traineeproject_prn'
    verbose_name = 'Traineeproject PRN'
    admin_site_name = 'traineeproject_prn_admin'


    # TODO: to include models