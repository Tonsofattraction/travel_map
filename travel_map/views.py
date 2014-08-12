'''
Created on Aug 11, 2014

@author: noob
'''

from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Country
import json
import logging

def home(request):
    logging.error("GGGGGGGGGGGGGGGGGGGGGGGG")
    return render_to_response('travel_map.html', context_instance=RequestContext(request))


def get_data(request):
    if request.method == 'GET':
        logging.error("DDDDDDDDDDDDDDDDDDDDDDD %s", Country.objects.all())
    
        data = json.dumps([{'value': int(c.value), 'name': c.name, 'code':c.code} for c in Country.objects.all()])
        logging.error(data)
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponseNotAllowed()
    
        
def visit(request):
    code = request.GET['code']
    country = Country.objects.get(code=code)
    if country.value:
        country.value = False
    else:
        country.value = True
    country.save()
    return HttpResponse()