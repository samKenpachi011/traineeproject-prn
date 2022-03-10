from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_url = '/administration/'
    enable_nav_sidebar = False
    site_header = 'TraineeProject PRN'
    site_title = 'TraineeProject PRN'
    index_title = 'TraineeProject PRN'

traineeproject_prn_admin = AdminSite(name='traineeproject_prn_admin')    