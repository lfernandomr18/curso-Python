import json 
from apiskeys import configuraciones
from Funciones import PartidaxId
import requests


api=configuraciones.apikeyopendota

salida=PartidaxId("5769042950",api)  

json_dataDePartida = json.loads(salida)


class Partida:
    match_id=None
    barracks_status_dire=None
    barracks_status_radiant=None
    replay_url=None

nuevapartida= Partida()
nuevapartida.match_id=json_dataDePartida['match_id']
nuevapartida.barracks_status_dire=json_dataDePartida['barracks_status_dire']
nuevapartida.barracks_status_radiant=json_dataDePartida['barracks_status_radiant']
nuevapartida.replay_url=json_dataDePartida['replay_url']

print(nuevapartida.match_id)
print(nuevapartida.barracks_status_dire)
print(nuevapartida.barracks_status_radiant)
print(nuevapartida.replay_url)





