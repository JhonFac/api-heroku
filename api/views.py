from django.http import JsonResponse, HttpResponse
from .models import Model_Forms
from django.views import View
import requests
import json 

class RequesForms(View):
    def hola(request):
        return HttpResponse('<h1>HOLA</h1>')

    def get(self, request):
        Clist= Model_Forms.objects.all()
        return JsonResponse(list(Clist.values()), safe=False)