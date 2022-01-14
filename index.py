from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pyautogui
import time
import getpass
from datetime import datetime, timedelta
from pathlib import Path



print("Iniciando navegador")
driver = webdriver.Chrome()
driver.get('https://rr1---sn-bg07dnky.googlevideo.com/videoplayback?expire=1642141424&ei=kMLgYeHcI4nChgadtbHgCg&ip=138.219.120.122&id=o-ABHfS7zAM5P6O14Gl5LDGRuszNL6v4WXhc2GxaZ28NMV&itag=22&source=youtube&requiressl=yes&vprv=1&mime=video%2Fmp4&ns=FvGmb7aG5yklNEZpEQca9AYG&cnr=14&ratebypass=yes&dur=6047.312&lmt=1588691066990302&fexp=24001373,24007246&c=WEB&txp=6316222&n=6CXu6xkXIzX_1Q&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgXDGGYP-yd150rVn7kLg32i0_Mx-1jRZBntZraXi369UCIQCEJklx3KOcL2t7CSsWDPzMSdj1MxTmPJgB6KfK9bbT6A%3D%3D&title=Selenium%20com%20Python%20%2304%20-%20Navega%C3%A7%C3%A3o%20e%20atributos&rm=sn-ab5eel7e&req_id=4f6f03cd8e90a3ee&ipbypass=yes&redirect_counter=2&cm2rm=sn-uv24pcg5-v2ne7e&cms_redirect=yes&mh=sE&mip=24.152.30.229&mm=29&mn=sn-bg07dnky&ms=rdu&mt=1642119677&mv=m&mvi=1&pl=24&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRAIgcgbY3rRfDI9r3HnJ2U2gaWytlzxRsXNxMgxdoQrnl8QCIAONWNUqDaYGeD2UOmCiGV8qDNlkcnrIB7fDkXL7wOow')
driver.get('chrome://downloads/')


controle = 0
def verificaDownload(controle):
    print("Verificando se Download foi concluido")
    
    while  controle == 0:
        time.sleep(2.0)
        print("Ainda baixando")
        concluido = driver.execute_script("""
            return document.querySelector('downloads-manager')
            .shadowRoot.querySelector('#downloadsList')
            .items.filter(e => e.state === 'COMPLETE')
            .map(e => e.filePath || e.file_path || e.fileUrl || e.file_url);
            """)
        controle = (len(concluido))

verificaDownload(0)

print("Download efetuado com sucesso")

        
        
