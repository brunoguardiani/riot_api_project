import api_lol.settings as settings
import requests


class DDragonServices():

    def __init__(self):
        self.url = settings.RIOT_API_URLS.DDRAGON_DATASET.value

    def get_champions_info(self):
        response = requests.get(f'{self.url}/data/en_US/champion.json')
        return response.json(), response.status_code
    
    