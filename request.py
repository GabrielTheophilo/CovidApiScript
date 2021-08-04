import requests
import json
class Request:
    def __init__(url, headers):
        response = requests.request("GET", url, headers=headers)
        json_data = response.json()
        data = json.dumps(json_data, indent=4)
        return data
class RequestHistorical:
    def __init__(url, headers, querystring):
        response = requests.request("GET", url, headers=headers, params=querystring)
        json_data = response.json()
        data = json.dumps(json_data, indent=4)
        
        return data
    