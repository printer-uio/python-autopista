from bs4 import BeautifulSoup
import requests


def consulta():
    dato=requests.get(url)
    dato1=BeautifulSoup(dato.text, "html.parser")
    valor = dato1.find_all('span')
    valor1=valor[2]
    valor2 = str(valor1)
    valor3 = valor2.replace('<span>','')
    global valor4
    valor4 = valor3.replace('</span>','')

url='https://serviciosagr.pichincha.gob.ec/ws-peaje/api/publico/consulta/saldo/placa/pdm1590'
consulta()
print ('KICS Placa: PDM1590 SALDO: ' + valor4)
url='https://serviciosagr.pichincha.gob.ec/ws-peaje/api/publico/consulta/saldo/placa/pbv4626'
consulta()
print ('FRONTIER Placa: PBV4626 SALDO: ' + valor4)
input("PRESIONE ENTER PARA SALIR")


    
