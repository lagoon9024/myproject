from django.shortcuts import render,HttpResponse,render_to_response
from .models import Detect
# Create your views here.
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import TemplateView
import random, json
import datetime
from django.db.models import Q

class detectdata(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name='detected_list.html'
        detected_list=Detect.objects.all()
        return render(request, template_name, {"detected_list" : detected_list})

def data_json(request):
    detected_list=Detect.objects.filter(cid='jh', cname='jh')
    Times = [None, ]
    Concentrations = ['percent',]
    Base=[None, ]
    for list in detected_list:
        Times.append(str(list.ctime))
        if list.cpercent>10:
            Concentrations.append(str(list.cpercent))
            
        else:
            Concentrations.append(0)
        Base.append(15)
    data = {
        'columns': [
            Times,
            Concentrations,
            Base,
        ]
    }
    return HttpResponse(json.dumps(data),content_type='text/json')
 
def main_page(request):
    return render_to_response('main_page.html')