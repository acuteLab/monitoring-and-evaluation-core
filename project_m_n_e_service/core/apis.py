from ninja import Router
from .views import Country, Currency

country_api = Router()


@country_api.get("/currencies")
def get_currencies(request):
    return Currency.get_currencies(request)

@country_api.get("/countries")
def get_countries(request):
    return Country.get_countries(request)


@country_api.get("/country")
def get_country(request, countryCode: str):
    return Country.get_country_by_code(request, countryCode)