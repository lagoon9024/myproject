from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

class user_account(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'login.html'
        return render(request, template_name)

    def post(self,request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username= username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('../')
            else:
                return render(request, 'login.html', {'error': 'username or password is incorrect'})
        else:
            return render(request, 'login.html')