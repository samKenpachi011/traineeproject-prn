from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_action_item import Action, HIGH_PRIORITY, site_action_items

DEATH_REPORT_ACTION = 'submit-death-report'
SUBJECT_OFFSTUDY_ACTION = 'submit-subject-offstudy'

"""
What is an action item : special forms
"""

class DeathReportAction(Action):
    name = DEATH_REPORT_ACTION
    display_name = 'Submit Death Report'
    reference_model = 'traineeproject_prn.deathreport'
    show_link_to_changelist = True
    show_link_to_add = True
    admin_site_name = 'traineeproject_prn_admin'
    priority = HIGH_PRIORITY
    singleton = True

    def get_next_actions(self):
        actions = []
        deathreport_cls = django_apps.get_model('traineeproject_prn.deathreport')

        subject_identifier = self.reference_model_obj.subject_identifier
        try:
            deathreport_cls.objects.get(subject_identifier=subject_identifier)
            actions = [SubjectOffStudyAction]
        except ObjectDoesNotExist:
            pass
        return actions

class SubjectOffStudyAction(Action):
    name = SUBJECT_OFFSTUDY_ACTION
    display_name = 'Enroll to sub-study'
    reference_model = 'myapp.enroll'
    show_link_to_changelist = True
    show_link_to_add = True
    admin_site_name = 'traineeproject_prn_admin'
    priority = HIGH_PRIORITY
    singleton=True

site_action_items.register(SubjectOffStudyAction)