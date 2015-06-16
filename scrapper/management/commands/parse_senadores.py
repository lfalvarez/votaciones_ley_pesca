# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import xml.etree.ElementTree as ET


class Command(BaseCommand):
    help = 'Parsea los votos de un proyecto de ley'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        tree = ET.parse(options['filename'][0])
        senadores = tree.getroot()
        for senador in senadores:
            parlid = senador.find('PARLID').text
            apellido_p = senador.find('PARLAPELLIDOPATERNO').text
            apellido_m = senador.find('PARLAPELLIDOMATERNO').text
            nombre = senador.find('PARLNOMBRE').text
            print parlid, nombre, apellido_p, apellido_m
