import api_lol.settings as settings
import requests


class ChampionMasteriesRiotApiServices():

    def __init__(self):
        self.url = settings.RIOT_API_URLS.CHAMPIONS_MASTERIES.value
        self.api_key = settings.API_KEY

    def get_top_champion_masteries(self, encrypted_summoner_id):
        response = requests.get(f'{self.url}/{encrypted_summoner_id}/top?count=3&api_key={self.api_key}')
        return response.json(), response.status_code
    
    