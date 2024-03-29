import re
import requests
from django.http import JsonResponse
from rest_framework.views import APIView, status
import api_lol.settings as settings

from api_lol.services.summoner import SummonerRiotApiServices
from api_lol.services.champion_masteries import ChampionMasteriesRiotApiServices
from api_lol.services.ddragon import DDragonServices
from api_lol.services.league import LeagueRankRiotApiServices


class RiotPlayer(APIView):
    def _get_champions_info(self, champions_ids):
        ddragon_services = DDragonServices()
        ddragon_response, ddragonq_response_status_code = ddragon_services.get_champions_info()
        champ_list = ddragon_response.get('data')
        dict_champions = {j['key']:j['name'] for i,j in champ_list.items() if j['key'] in champions_ids}
        return dict_champions

    def __sanitize_champions_names(self, champions_list):
        for champion_id, champion_name in champions_list.items():
            champion_names = [champion_name]
            if "'" in champion_name:
                champion_names = champion_name.split("'")
            elif " " in champion_name:
                champion_names = champion_name.split(' ')
            champions_list[champion_id] = ''.join([partial_name.capitalize() for partial_name in champion_names])
        return champions_list

    def _get_champions_masteries_list(self, champions_masteries, ddragon_version):
        champions_ids = [str(cm.get('championId')) for cm in champions_masteries]
        cm_dict = self.__sanitize_champions_names(self._get_champions_info(champions_ids))
        cm_result = [\
                    {
                        'champion_name':cm_dict.get(str(champ.get('championId'))),
                        'champion_level_mastery': champ.get('championLevel'),
                        'champion_mastery_points' : champ.get('championPoints'),
                        'champion_icon': f"{settings.RIOT_API_URLS.DDRAGON_DATASET.value}/{ddragon_version}/img/champion/{cm_dict.get(str(champ.get('championId')))}.png"
                    } for champ in champions_masteries]
        return cm_result

    def _get_tier_image(self, summoner_tier_list):
        for i in summoner_tier_list:
            i['tier_image'] = None
            if i.get("tier", None):
                tier = i.get("tier").lower()
                i['tier_image'] = f'{settings.RIOT_API_URLS.TIER_IMAGES_URL.value}/{tier}.png'
        
        return summoner_tier_list

    def get(self, request, *args, **kwargs):
        summoner_name = kwargs['username']
        ddragon_service = DDragonServices()
        ddragon_version = ddragon_service.get_ddragon_version()[0]
        summoner_service = SummonerRiotApiServices()
        acnt_response, acnt_response_status_code = summoner_service.get_summoner_by_name(summoner_name)

        if acnt_response_status_code != 200:
            return JsonResponse({f'error':acnt_response}, status=acnt_response_status_code)

        encrypted_summoner_id = acnt_response.get('id')

        cm_service = ChampionMasteriesRiotApiServices()
        champion_masteries_response, champion_masteries_response_status_code = cm_service.get_top_champion_masteries(encrypted_summoner_id)

        if champion_masteries_response_status_code != 200:
            return JsonResponse({f'error':champion_masteries_response}, status=champion_masteries_response_status_code)

        champ_result_list = {'champion_masteries':self._get_champions_masteries_list(champion_masteries_response, ddragon_version)}

        league_service = LeagueRankRiotApiServices()
        ranked_info_response, ranked_info_response_status_code = league_service.get_rank_info_by_id(encrypted_summoner_id)
        if ranked_info_response_status_code != 200:
            return JsonResponse({f'error':ranked_info_response}, status=ranked_info_response_status_code)

        enriched_ranked_info = {'tiers':self._get_tier_image(ranked_info_response)}

        dict_result = {**acnt_response, **champ_result_list, **enriched_ranked_info}
        prf_id = acnt_response.get('profileIconId')
        dict_result['profile_image'] = f'{settings.RIOT_API_URLS.DDRAGON_DATASET.value}/{ddragon_version}/img/profileicon/{prf_id}.png'
        return JsonResponse(dict_result, status=status.HTTP_200_OK)

class RiotTopChallengers(APIView):
    def get(self, request, *args, **kwargs):
        pass