from ninja import Router
from .views import Country

country_api = Router()

@country_api.get("/countries")
def get_countries(request):
    return Country.get_countries(request)


@country_api.get("/country")
def get_country(request, countryCode: str):
    return Country.get_country_by_code(request, countryCode)