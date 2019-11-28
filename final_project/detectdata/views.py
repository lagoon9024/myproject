from django.shortcuts import render,HttpResponse,render_to_response
from .models import Detect
# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from django.views import generic
from django.views.generic import TemplateView
import random, json
import datetime
from django.db.models import Q

class detectdata(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name='data.html'
        return render(request, template_name)
    
def data_json(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    detected_list=Detect.objects.filter(cid=username, cname=username)
    Times = [None, ]
    Concentrations = ['percent',]
    for list in detected_list:
        Times.append(str(list.ctime))
        if list.cpercent>10:
            Concentrations.append(str(list.cpercent))
        else:
            Concentrations.append(0)
    data = {
        'columns': [
            Times,
            Concentrations,
        ]
    }
    return HttpResponse(json.dumps(data),content_type='text/json')
 
def main_page(request):
    return render_to_response('data.html')
