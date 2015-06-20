# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import xml.etree.ElementTree as ET
from unidecode import unidecode
from popolo.models import Person, Identifier, OtherName


class Command(BaseCommand):
    help = 'Parsea los votos de un proyecto de ley'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        tree = ET.parse(options['filename'][0])
        senadores = tree.getroot()
        for senador in senadores:
            apellido_p = senador.find('PARLAPELLIDOPATERNO').text
            apellido_m = senador.find('PARLAPELLIDOMATERNO').text
            nombre = senador.find('PARLNOMBRE').text
            p, created = Person.objects.get_or_create(name="%s %s %s" % (nombre, apellido_p, apellido_m), family_name="%s %s" % (apellido_p, apellido_m), given_name=nombre)
            if created:
                parlid = senador.find('PARLID').text
                identifier = Identifier.objects.create(identifier=parlid)
                p.identifiers.add(identifier)
                simple_name = "%(apellido_p)s %(apellido_m)s., %(nombre)s" % {"apellido_p": apellido_p, "apellido_m": apellido_m[0], "nombre": nombre}  # Chahuán C., Francisco
                other_name = OtherName.objects.create(name=simple_name)
                p.other_names.add(other_name)
                other_name = OtherName.objects.create(name=unidecode(simple_name))  # Chahuan C., Francisco
                p.other_names.add(other_name)
