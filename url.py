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
        'x-rapidapi-key': "2411691043msh014509ac5829fc6p190baajsn4375908ad913",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

