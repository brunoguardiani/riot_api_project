from rest_framework.views import APIView
from django.http import JsonResponse
import requests
from rest_framework import status


class RiotPlayer(APIView):
    def get_champion_info(self, champion_id):
        champions_ids = requests.get('http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json')
        champ_list = champions_ids.json().get('data')
        for i,j in champ_list.items():
            if j['key'] == champion_id:
                return j['name']

    def get(self, request, *args, **kwargs):
        summoner_name = kwargs['username']
        acnt_response = requests.get(f'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key=RGAPI-3540c9b8-3471-4e1f-8a3c-f2c94797480d')
        if acnt_response.status_code != 200:
            return JsonResponse({f'error':{acnt_response.json()}}, status=acnt_response.status_code)
        encrypted_summoner_id = acnt_response.json().get('id')
        mst_response = requests.get(f'https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encrypted_summoner_id}/top?count=3&api_key=RGAPI-3540c9b8-3471-4e1f-8a3c-f2c94797480d')
        champ_result_list = []
        for champ in mst_response.json():
            champion_name = self.get_champion_info(str(champ.get('championId')))
            champ_result_list.append({
                'champion_name' : champion_name,
                'champion_level_mastery' : champ.get('championLevel'),
                'champion_mastery_points' : champ.get('championPoints'),
                'champion_icon': f'http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/{Aatrox}.png'
            })
        acnt_response = acnt_response.json()
        prf_id = acnt_response.get('profileIconId')
        acnt_response['profile_image'] = f'http://ddragon.leagueoflegends.com/cdn/10.15.1/img/profileicon/{prf_id}.png'
        acnt_response['champion_masteries'] = champ_result_list
        return JsonResponse(acnt_response, status=mst_response.status_code)

