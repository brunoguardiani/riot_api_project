import api_lol.settings as settings
import requests


class DDragonServices():

    def __init__(self):
        self.url = settings.RIOT_API_URLS.DDRAGON_DATASET.value

    def get_ddragon_version(self):
        response = requests.get(f'https://ddragon.leagueoflegends.com/api/versions.json')
        return response.json()[0], response.status_code
        
    def get_champions_info(self):
        ddragon_version = self.get_ddragon_version()[0]
        response = requests.get(f'{self.url}/{ddragon_version}/data/en_US/champion.json')
        return response.json(), response.status_code
    