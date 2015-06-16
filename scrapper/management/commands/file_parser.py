# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import xml.etree.ElementTree as ET

SELECCION = {
    'si': True,
    'no': False,
    'pareo': 'PAREO',
    'abstencion': None
}


class Command(BaseCommand):
    help = 'Parsea los votos de un proyecto de ley'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        tree = ET.parse(options['filename'][0])
        votaciones = tree.getroot()
        for votacion in votaciones:
            fecha = votacion.find('FECHA').text
            sesion = votacion.find('SESION').text
            tema = votacion.find('TEMA').text
            si = votacion.find('SI').text
            no = votacion.find('NO').text
            abstencion = votacion.find('ABSTENCION').text
            pareo = votacion.find('PAREO').text
            quorum = votacion.find('QUORUM').text
            try:
                tipo_votacion = votacion.find('TIPOVOTACION').text
            except:
                tipo_votacion = ''
            etapa = votacion.find('ETAPA').text
            for voto in votacion.find('DETALLE_VOTACION'):
                parlamentario = voto.find('PARLAMENTARIO').text
                seleccion = voto.find('SELECCION').text.lower()
                
