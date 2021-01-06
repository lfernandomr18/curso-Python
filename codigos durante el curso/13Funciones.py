import requests
import  configuraciones

api=configuraciones.apikeyopendota


def descargarPartidaxId(idpartida,api):
    
    if __name__=='__main__':
        url='https://api.opendota.com/api/matches/'+idpartida+'?'+api
        
        response=requests.get(url)

        if response.status_code==200:
            contenidoRespApi=response.content
            file=open(idpartida+'.html','wb')
            file.write(contenidoRespApi)
            file.close()
            print('se ha obtenido el archivo de la partida %s correctamente'%(idpartida))
        else :
            print('Error: STATUS ')

descargarPartidaxId('5773559310',api)