import sys

import requests
apikeyopendota='7252eea3-1d88-4e37-9ad7-daa31c8c31d0'
##aca trae toma el argumento que se pasa desde el cmd
idpartida=sys.argv[1]

if __name__=='__main__':
    url='https://api.opendota.com/api/matches/'+idpartida+'?'+apikeyopendota
    
    response=requests.get(url)

    if response.status_code==200:
        contenidoRespApi=response.content
        file=open(idpartida+'.html','wb')
        file.write(contenidoRespApi)
        file.close()
        print('se ha obtenido el archivo de la partida %s correctamente'%(idpartida))
    else :
        print('Error: STATUS ')

