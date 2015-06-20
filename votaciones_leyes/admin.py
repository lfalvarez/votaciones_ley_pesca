from django.contrib import admin
from popolo.models import Person, OtherName, Organization
from django.contrib.contenttypes.admin import GenericTabularInline
from votaciones_leyes.models import ProyectoDeLey, Motion, VoteEvent, Vote
# Register your models here.


class OtherNameInline(GenericTabularInline):
    model = OtherName


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [OtherNameInline, ]


@admin.register(OtherName)
class OtherNameAdmin(admin.ModelAdmin):
    pass


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(ProyectoDeLey)
class ProyectoDeLeyAdmin(admin.ModelAdmin):
    pass


@admin.register(Motion)
class MotionAdmin(admin.ModelAdmin):
    pass


@admin.register(VoteEvent)
class VoteEventAdmin(admin.ModelAdmin):
    pass


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass
