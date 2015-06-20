from django import template
from votaciones_leyes.models import Vote

register = template.Library()


@register.inclusion_tag('votes_per_candidate.html')
def show_votes(motion, candidate):
    votes = Vote.objects.filter(voter=candidate, vote_event__motion=motion)
    return {'votes': votes}