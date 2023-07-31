from django.shortcuts import render
from django.views import View
from .forms import (
    AuthorForm
)
# Create your views here.
class BooksList(View): 

    def __init__(self):
        self.template = 'books.html'
        
    def get(self, request):

        context = {
            'prueba': 'prueba'
        }

        return render(request, self.template, context)
    
class BooksDashboard(View): 

    def __init__(self):
        self.template = 'books_dashboard.html'
        
    def get(self, request):

        context = {
            'prueba': 'prueba'
        }

        return render(request, self.template, context)
    
class GenderList(View): 

    def __init__(self):
        self.template = 'gender.html'
        
    def get(self, request):

        context = {
            'prueba': 'prueba'
        }

        return render(request, self.template, context)
    
class EditorialList(View): 

    def __init__(self):
        self.template = 'editorial.html'
        
    def get(self, request):

        context = {
            'prueba': 'prueba'
        }

        return render(request, self.template, context)
    
class AuthorList(View): 

    def __init__(self):
        self.template = 'author.html'
        
    def get(self, request):

        form = AuthorForm
        context = {
            'form': form
        }

        return render(request, self.template, context)
    
    
class CategoriesList(View): 

    def __init__(self):
        self.template = 'category.html'
        
    def get(self, request):

        context = {
            'prueba': 'prueba'
        }

        return render(request, self.template, context)
    
    
class ShelvesList(View): 

    def __init__(self):
        self.template = 'shelve.html'
        
    def get(self, request):

        context = {
            'prueba': 'prueba'
        }

        return render(request, self.template, context)
    