from apikey import ApiKey
class UrlGeneral(ApiKey):
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        'x-rapidapi-key': f'{ApiKey.ApiKey}',
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }
class UrlHistorical(ApiKey):
    url = "https://covid-193.p.rapidapi.com/history"

    headers = {
        'x-rapidapi-key': f"{ApiKey.ApiKey}",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

