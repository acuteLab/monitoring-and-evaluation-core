import json

class Country:
    def __init__(self):
          pass
    countries = []
    with open('config/countries.json') as json_file:
       countries = json.load(json_file)
      
    def get_countries(request, countries=countries):
        try:
            return countries
        except:
            raise "Inernal Server Error"
        
    def get_country_by_code(request, country_code, countries=countries):
        try:
            country_code = country_code.upper()
            return countries[country_code]
        except:
            raise "Inernal Server Error"
    
class Currency:
    def __init__(self):
          pass
    countries = Country.countries
    
    def  get_currencies(request, countries = countries):
        try:
            return [{"country": country["countryName"], "currency": country["currencyCode"]} for country in countries]
        except:
            raise "Internal server Error"

    
        