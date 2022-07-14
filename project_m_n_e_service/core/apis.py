from ninja import Router
from .views import Country

country_api = Router()

@country_api.get("/countries")
def get_countries(request):
    return Country.get_countries(request)
