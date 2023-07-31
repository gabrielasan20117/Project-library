from django.shortcuts import render
from django.views import View
# Create your views here.
class Home(View): 

    def __init__(self):
        self.template = 'home/home.html'
        
    def get(self, request):

        context = {
            'prueba': 'prueba'
        }

        return render(request, self.template, context)
    