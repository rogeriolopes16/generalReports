import mysql.connector
import json
import csv
from datetime import datetime
from settings.credentials import *
from settings.parameters import *
from settings.db import *

sysdate = datetime.now().strftime('%d/%m/%Y')
sysdateWSO2 = datetime.now().strftime('%m%Y')

print(str(datetime.now().strftime('%d/%m/%Y-%H:%M:%S')+': Inicio da atividade'))

# --------------------------- Abrindo conexão com MYSql Blazon ---------------------------
db = mysql.connector.connect(user=CRD_USER_DB_BLAZON, passwd=CRD_PWD_DB_BLAZON, host=PAR_BLAZON_IP, db=PAR_BLAZON_DB_NAME)
cursor_blazon = db.cursor()

# fazendo select para encontrar usuarios no blazon
cursor_blazon.execute(SELECT_USERS_ACTIVES_BLAZON)
blazon = cursor_blazon.fetchall()

with open('c:/Automations/generalReports/accountsR12eSomar/reports/AccountsR12eSomar.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["NOME", "USUARIO", "SISTEMA","STATUS"])

    # verifica nome faltantes no R12 e busca no blazon, criando uma nova lista atualizada
    for blazonfor in blazon:
        writer.writerow([blazonfor[0], blazonfor[1], blazonfor[2], blazonfor[3]])

print(str(datetime.now().strftime('%d/%m/%Y-%H:%M:%S')+': Fim da atividade'))
