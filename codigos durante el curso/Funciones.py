import requests
from apiskeys import configuraciones

api=configuraciones.apikeyopendota


def descargarPartidaxId(idpartida,api):
    
    if __name__=='__main__':
        url='https://api.opendota.com/api/matches/'+idpartida+'?'+api
        
        response=requests.get(url)

        if response.status_code==200:
            contenidoRespApi=response.content
            file=open(idpartida+'.JSON','wb')
            file.write(contenidoRespApi)
            file.close()
            print('se ha obtenido el archivo de la partida %s correctamente'%(idpartida))
        else :
            print('Error: STATUS ')



def PartidaxId(idpartida,api):
    contenidoRespApi2=None
    if __name__==__name__:
        url='https://api.opendota.com/api/matches/'+idpartida+'?'+api
        
        response=requests.get(url)

        if response.status_code==200:
          
            contenidoRespApi2=response.text
          
        else :
            print('Error: STATUS ')
    return contenidoRespApi2
        

        


