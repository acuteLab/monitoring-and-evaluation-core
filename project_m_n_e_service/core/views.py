from django.shortcuts import render
from django_countries import countries

class Country:
    def __init__(self):
          pass
      
    def get_countries(request):
        try:
          return list(countries)
        except:
            return "Inernal Server Error"