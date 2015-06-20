# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import xml.etree.ElementTree as ET
from unidecode import unidecode
from popolo.models import Person, OtherName


def nombre_completo_parser(nombre_completo):
    nombres_apellidos = nombre_completo.split(',')
    apellidos_ = nombres_apellidos[0]
    nombre = nombres_apellidos[1].strip()
    if len(apellidos_.split(" ")) > 2:
        ap = apellidos_.split(" ")
        apellido_p = ap[0]
        apellido_m = ap[2]
        return nombre, apellido_p, apellido_m
    else:
        apellido_p, apellido_m = apellidos_.split(" ")
    return nombre, apellido_p, apellido_m


class Command(BaseCommand):
    help = 'Parsea los votos de un proyecto de ley'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        tree = ET.parse(options['filename'][0])
        senadores = tree.getroot()
        for senador in senadores:
            nombre_completo = senador.find('NOMBRECOMPLETO').text
            if nombre_completo_parser(nombre_completo):
                nombre, apellido_p, apellido_m = nombre_completo_parser(nombre_completo)

                p, created = Person.objects.get_or_create(name=u"%s %s %s" % (nombre, apellido_p, apellido_m), family_name=u"%s %s" % (apellido_p, apellido_m), given_name=nombre)
                if created:
                    simple_name = "%(apellido_p)s %(apellido_m)s., %(nombre)s" % {"apellido_p": apellido_p, "apellido_m": apellido_m[0], "nombre": nombre}  # Chahuán C., Francisco
                    other_name = OtherName.objects.create(name=simple_name)
                    p.other_names.add(other_name)
                    other_name = OtherName.objects.create(name=unidecode(simple_name))
                    p.other_names.add(other_name)
