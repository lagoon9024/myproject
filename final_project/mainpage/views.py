from django.shortcuts import render, redirect
from django.views import View
from django.views import generic

class main_page(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'index.html'
        return render(request, template_name)

