from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from popolo.models import Person
from votaciones_leyes.models import ProyectoDeLey, Motion


class PersonListView(ListView):
    model = Person
    template_name = 'home.html'


class PersonDetailView(DetailView):
    model = Person
    template_name = 'votaciones.html'
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        proyectos = ProyectoDeLey.objects.all()
        votaciones = {}
        for proyecto in proyectos:

            for motion in proyecto.motion_set.all():
                votaciones[motion.id] = []
                for event in motion.vote_events.all():
                    for vote in event.vote_set.filter(voter=self.object):
                        votaciones[motion.id].append(vote)
        context['votaciones'] = votaciones
        context['proyectos'] = proyectos
        return context


