#IMPORTACION DE LIBRERIAS#
import pandas as pd #Importacion del modulo pandas para el manejo de archivos csv

#LECTURA DE ARCHIVO CSV#
df = pd.read_csv("../data/data.csv")#Leer el archivo data.csv y obtener sus datos

#CALCULO DEL BALANCE FINAL#
suma_credito=df[df['tipo']=='Crédito']['monto'].sum()#Sumar el monto de las transacciones de tipo Crédito
suma_debito=df[df['tipo']=='Débito']['monto'].sum()#Sumar el monto de las transacciones de tipo Débito
balance_final=suma_credito-suma_debito#obtemos el balance final, restando el monto de la suma_credito y suma_debito

#CALCULO DE LA TRANSACCION DE MAYOR MONTO#
fila_maxima = df.loc[df['monto'].idxmax()]#Obtenemos el indice de la fila con el monto maximo, nos retorna un objeto
id = fila_maxima['id']#Obtenemos del objeto fila_maxima el id
monto = fila_maxima['monto']##Obtenemos del objeto fila_maxima el monto

#CALCULO DEL TOTAL DE CADA TIPO DE TRANSACCIONES#
tipo_credito=df[df['tipo']=='Crédito']['tipo'].count()#Obtenemos el total de transacciones de tipo Crédito
tipo_debito=df[df['tipo']=='Débito']['tipo'].count()#Obtenemos el total de transacciones de tipo Débito

#REPORTE FINAL#
print("""Reporte de Transacciones
---------------------------""")#Mostramos el titulo
print(f"Balance Final: {balance_final:.2f}")#Mostramos el balance final (redondeamos el valor con dos decimales)
print(f"Transacción de Mayor Monto: ID {id} - {monto}")#Mostramos la transaccion de mayor monto
print(f"Conteo de Transacciones: Crédito: {tipo_credito} Débito: {tipo_debito}")#Mostramos el conteo de las transacciones 
