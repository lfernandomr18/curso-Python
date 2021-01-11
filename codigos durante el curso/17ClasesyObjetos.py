import json 
from apiskeys import configuraciones
from Funciones import PartidaxId
import requests



api=configuraciones.apikeyopendota

salida=PartidaxId("5769042950",api)  

json_dataDePartida = json.loads(salida)

## esto es una clase
class Partida:
    match_id=None
    barracks_status_dire=None
    barracks_status_radiant=None
    replay_url=None
    players=[]
    #esto permite inicializar mi objeto 
    def __init__(self,match_id,barracks_status_dire,barracks_status_radiant,replay_url,players):
        self.match_id=match_id
        self.barracks_status_dire=barracks_status_dire
        self.barracks_status_radiant=barracks_status_radiant
        self.replay_url=replay_url
        cont=len(players)
        for i in players:
            if players[cont-1]['account_id'] != None:
                self.players.append(players[cont-1]['account_id'])
            cont=cont-1
            

        salida=' '.join(map(str, self.players))
        print('se ha creado el objeto de la partida: %d, las barracas:%d,%d y los jugadores:'%(match_id,barracks_status_dire,barracks_status_radiant)+salida)

nuevapartida= Partida(json_dataDePartida['match_id'],json_dataDePartida['barracks_status_dire'],json_dataDePartida['barracks_status_radiant'],json_dataDePartida['replay_url'],json_dataDePartida['players'])



