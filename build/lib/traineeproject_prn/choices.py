from edc_constants.constants import OTHER


OFF_STUDY_REASON = (
    ('death', 'Patient death'),
    ('sponsor_terminated', 'Study terminated by sponsor'),
    ('ltfu', 'Patient lost to follow up'),
    ('subject_withdrawal', 'Withdrawal by subject'),
    ('adverse_event', 'Adverse Event'),
    (OTHER, 'Other (specify)')

)

PLACE_OF_DEATH = (
    ('home_or_community', 'Home or in the community'),
    ('facility', 'At facility'),
    ('unknown', 'Place of death unknown')
)

DEATH_INFO_SOURCE = (
    ('death_certificate_review', 'Death Certificate Review'),
    ('clinician', 'Clinician'),
    ('next_of_kin1', 'Next of kin 1'),
    ('inpatient_medical_file', 'Inpatient medical file'),
    ('fam_member', 'family member (specify relationship)'),
    (OTHER, 'Other (specify)'),
)

CAUSE_OF_DEATH_CAT = (
    ('study_drug', 'Toxicity from Study Drug'),
    ('non_study_drug', 'Toxicity from non-Study drug'),
    ('trauma', 'Trauma/Accident'),
    ('no_info', 'No information available'),
    (OTHER, 'Other, specify'),)

MED_RESPONSIBILITY = (
    ('doctor', 'Doctor'),
    ('nurse', 'Nurse'),
    ('traditional', 'Traditional Healer'),
    ('all', 'Both Doctor or Nurse and Traditional Healer'),
    ('none', 'No known medical care received (family/friends only)'),)

HOSPITALIZATION_REASON = (
    ('covid19_related_symptoms', 'COVID-19 related symptoms'),
    (OTHER, 'Other'),
)

FACILITY = (
    ('athlone_hospital', 'Athlone Hospital'),
    ('bamalete_lutheran_hospital', 'Bamalete Lutheran Hospital'),)
