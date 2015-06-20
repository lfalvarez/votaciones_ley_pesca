# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import xml.etree.ElementTree as ET
from unidecode import unidecode
from popolo.models import Person, Identifier, Organization
from django.db.models import Q
import time
from votaciones_leyes.models import ProyectoDeLey, Motion, VoteEvent, Vote
import hashlib

SELECCION = {
    'si': 'yes',
    'no': 'no',
    'pareo': 'paired',
    'abstencion': 'abstain',
    'ausente': 'Absent',
    'not_voting': 'Not voting'
}


class Command(BaseCommand):
    help = 'Parsea los votos de un proyecto de ley'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        proyecto, created = ProyectoDeLey.objects.get_or_create(boletin=options['filename'][0].split('.')[0])
        senado = Organization.objects.get(id='senado-de-chile')
        tree = ET.parse(options['filename'][0])
        votaciones = tree.getroot()
        for votacion in votaciones:
            fecha_ = votacion.find('FECHA').text
            fecha = time.strptime(fecha_, "%d/%m/%Y")
            sesion = votacion.find('SESION').text
            tema = votacion.find('TEMA').text
            si = votacion.find('SI').text
            no = votacion.find('NO').text
            abstencion = votacion.find('ABSTENCION').text
            pareo = votacion.find('PAREO').text
            quorum = votacion.find('QUORUM').text
            motion, created = Motion.objects.get_or_create(legislative_session=sesion, text=tema, proyecto_de_ley=proyecto)
            if created:
                hash_object = hashlib.md5(sesion + unidecode(tema))
                identifier = hash_object.hexdigest()

                identifier = Identifier.objects.create(identifier=identifier)
                motion.identifiers.add(identifier)
            votacion_event, created = VoteEvent.objects.get_or_create(organization=senado, legislative_session=sesion, motion=motion)
            try:
                tipo_votacion = votacion.find('TIPOVOTACION').text
            except:
                tipo_votacion = ''
            etapa = votacion.find('ETAPA').text
            for voto in votacion.find('DETALLE_VOTACION'):
                seleccion = voto.find('SELECCION').text.lower()
                seleccion = SELECCION[seleccion]
                parlamentario = voto.find('PARLAMENTARIO').text.strip()
                query = Q(other_names__name=parlamentario) | Q(other_names__name=unidecode(parlamentario))
                persons = Person.objects.filter(query).distinct()
                if persons:
                    if persons.count() > 1:
                        print u"Este tipo está más veces de las que debería estar" + parlamentario
                    else:
                        person = persons.first()
                    voto, created = Vote.objects.get_or_create(vote_event=votacion_event, voter=person, option=seleccion)
                else:
                    print u"No encontré a este tipo " + parlamentario
