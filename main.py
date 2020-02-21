import logging
from api import PixabayAPI
import sys
import threading

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

carpeta_imagenes = './imagenes'
query = sys.argv[1]
cantidad = sys.argv[2]



api = PixabayAPI('15310666-eb71639a97acfdc054f1c9662', carpeta_imagenes)

logging.info(f'Buscando {cantidad} imagenes de {query}')
urls = api.buscar_imagenes(query, cantidad)


for u in urls:
  logging.info(f'Descargando {u}')
  api.descargar_imagen(u)
  #lambda sería como un closure "función"
  #threading.Thread(target = (lambda: api.descargar_imagen(u))).start()

logging.info(api.lista_imagenes)  