import requests

url = 'https://39f7f49eb703458a-dot-us-east1.notebooks.googleusercontent.com/lab?authuser=0&username=Alejandro_Espinal_Restrepo'
nombre_archivo_local = 'Untitled.ipynb'

# Realizar la solicitud GET al servidor para obtener el contenido del archivo
respuesta = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if respuesta.status_code == 200:
    # Abrir el archivo local en modo binario y escribir el contenido descargado
    with open(nombre_archivo_local, 'wb') as archivo_local:
        archivo_local.write(respuesta.content)
    print(f'El archivo {nombre_archivo_local} ha sido descargado exitosamente.')
else:
    print(f'Error al descargar el archivo. Código de estado: {respuesta.status_code}')
