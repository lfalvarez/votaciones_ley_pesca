from django.db import models
from popolo.models import Person, Organization, Identifier
from django.contrib.contenttypes import generic


class ProyectoDeLey(models.Model):
    boletin = models.CharField(max_length=512)


class Motion(models.Model):
    legislative_session = models.CharField(max_length=512, null=True)
    creator = models.ForeignKey(Person, null=True)
    text = models.TextField()
    identifiers = generic.GenericRelation(Identifier, help_text="Issued identifiers")
    proposal_date = models.DateField(null=True)
    requirement = models.TextField()
    result = models.CharField(max_length=512)

    proyecto_de_ley = models.ForeignKey(ProyectoDeLey, null=True)


class VoteEvent(models.Model):
    legislative_session = models.CharField(max_length=512, null=True)
    identifiers = generic.GenericRelation(Identifier, help_text="Issued identifiers")
    motion = models.ForeignKey(Motion, related_name="vote_events", null=True)
    organization = models.ForeignKey(Organization, null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

OPTION_CHOICES = (('yes', 'Yes'),
                  ('no', 'No'),
                  ('abstain', 'Abstain'),
                  ('absent', 'Absent'),
                  ('not_voting', 'Not voting'),
                  ('paired', 'Paired'),
                  )


class Vote(models.Model):
    vote_event = models.ForeignKey(VoteEvent, null=True)
    voter = models.ForeignKey(Person, null=True)
    option = models.CharField(max_length=512, choices=OPTION_CHOICES)
    political_group = models.ForeignKey(Organization, null=True)
    role = models.CharField(max_length=512, null=True)
