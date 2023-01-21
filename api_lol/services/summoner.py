import api_lol.settings as settings
import requests


class SummonerRiotApiServices():

    def __init__(self):
        self.url = settings.RIOT_API_URLS.SUMMONER_V4_URL.value
        self.api_key = settings.API_KEY

    def get_summoner_by_name(self, summoner_username):
        response = requests.get(f'{self.url}/by-name/{summoner_username}?api_key={self.api_key}')
        return response.json(), response.status_code
    
    