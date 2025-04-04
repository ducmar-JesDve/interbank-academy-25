# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Introducción:

Este reto permite obtener un reporte final de transacciones bancarias y su proposito es brindar información consolidada hacerca del Balance Final, Transacción de Mayor Monto y Conteo de transacciones

---

## Instrucciones de Ejecución: 

1. **Repositorio:**  
   Clona o haz un fork del repositorio disponible en:  
   `https://github.com/ducmar-JesDve/interbank-academy-25.git`

2. **Instalar dependencias:**  
   Antes de ejecutar el proyecto, verifica si tienes instalado pandas en tu maquina con el siguiente comando en el CMD: 

   ```
   pip show pandas
   ```
   Si lo tienes, el comando te dara toda la informacion, desde la version y ubicacion.
   Si no lo tienes, instalalo con el siguiente comando en el CMD: 

   ```
   pip install pandas
   ```

3. **Ejecutar el proyecto:**  
   Para ejecutar el proyecto, debe abrir la carpeta o estar en la ruta del archivo .py la aplicación debe mostrar el reporte final en la terminal.  
   Ejemplo de salida al ejecutar "python procesamientoBancario.py"

   ```
   Reporte de Transacciones
   ---------------------------------------------
   Balance Final: 10985.85
   Transacción de Mayor Monto: ID 222 - 499.69
   Conteo de Transacciones: Crédito: 508 Débito: 492
   ```

---

## Enfoque y Solución:
Para la solución del reto, obte por usar pandas para manejar el archivo csv de manera mas rapida; ademas, use funciones prodias de pandas que permitieron obtener los resultados. 

Para ello segui los siguientes pasos:

Lectura del csv.
Calculo del Balance Final.
Transaccion de Mayor Monto.
Conteo de Transacciones.
Presentación del informe.

---

## Estructura del Proyecto:
El proyecto tiene la siguiente estructura: 
   ```
   /interbank-academy-25 # Nombre de la carpeta principal
   │
   ├── /data                           # Carpeta que contiene el archivo CSV
   │   └──data.csv                     # Archivo CSV
   │
   ├── /scripts                        # Codigo fuente de la aplicacion
   │   └── procesamientoBancario.py    # Archivo principal para ejecutar el proyecto
   |
   └── README.md                       # Este archivo
   ```
