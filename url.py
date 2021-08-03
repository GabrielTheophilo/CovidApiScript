from apikey import ApiKey
class Url(ApiKey):
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        'x-rapidapi-key': f'{ApiKey.ApiKey}',
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }