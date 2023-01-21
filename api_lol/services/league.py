import api_lol.settings as settings
import requests


class LeagueRankRiotApiServices():

    def __init__(self):
        self.url = settings.RIOT_API_URLS.LEAGUE_V4_URL.value
        self.api_key = settings.API_KEY

    def get_rank_info_by_id(self, encrypted_summoner_id):
        print(f'{self.url}/entries/by-summoner/{encrypted_summoner_id}&api_key={self.api_key}')
        response = requests.get(f'{self.url}/entries/by-summoner/{encrypted_summoner_id}?api_key={self.api_key}')
        return response.json(), response.status_code
    
    