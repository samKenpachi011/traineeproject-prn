import imp
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.views.generic.base import RedirectView
from .admin_site import traineeproject_prn_admin


urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.APP_NAME == 'traineeproject_prn':
    from django.contrib import admin

    urlpatterns += [
        path('', amdin.s)
    ]
