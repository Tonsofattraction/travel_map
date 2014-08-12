'''
Created on Aug 11, 2014

@author: noob
'''

import logging
from ...models import Country
from ...world import countries as data
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    
    help = 'adds new countries'
    
    def handle(self, *args, **options):
        logging.info("GGGGGGGGGGGGGGGGGGGGGGGGGGG %s", data)
        for c in data:
            if not Country.objects.filter(name = c['name'], code = c['code']):
                Country.objects.create(name = c['name'],
                                       code = c['code']) 
            else:
                pass