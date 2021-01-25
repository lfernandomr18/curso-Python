import sys

sys.path.append("..")
from configuraciones import apikeyopendota
import requests

##aca trae toma el argumento que se pasa desde el cmd
idpartida=sys.argv[1]

if __name__=='__main__':
    url='https://api.opendota.com/api/matches/'+idpartida+'?'+apikeyopendota
    
    response=requests.get(url)

    if response.status_code==200:
        contenidoRespApi=response.content
        file=open(idpartida+'.JSON','wb')
        file.write(contenidoRespApi)
        file.close()
        print('se ha obtenido el archivo de la partida %s correctamente'%(idpartida))
    else :
        print('Error: STATUS ')
