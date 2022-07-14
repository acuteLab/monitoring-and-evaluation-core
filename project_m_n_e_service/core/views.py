from django.shortcuts import render
from django_countries import countries

class Country:
    def __init__(self):
          pass
      
    def get_countries(request):
        try:
          return [{'country_code': country_code, 'country_name': country_name} for country_code, country_name in  list(countries)]
        except:
            raise "Inernal Server Error"
        
    def get_country_by_code(request, country_code):
        try:
            return {'country_code': country_code, 'country_name': dict(countries)[country_code]}
        except:
            raise "Inernal Server Error"