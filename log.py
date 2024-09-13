import pandas as pd
from dateutil.relativedelta import relativedelta
from datetime import datetime
import logging

# Configurar el logger
logging.basicConfig(
    filename='log.log',  # Nombre del archivo de log
    level=logging.INFO,  # Nivel de registro (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato del mensaje
)

class LogOut:
   def task(self):
    # ingresar tarea principal del proceso
    task = pass

    # Leer el archivo de log
    log_df = pd.read_csv('log.log', 
                        sep=' - ',           # Usamos el separador que definiste en el log
                        header=None,          # No hay encabezado, lo definimos manualmente
                        names=['Fecha', 'Nivel', 'Mensaje'],  # Columnas personalizadas
                        engine='python',      # Usamos el engine python para separadores complejos 
                        encoding='utf-8')     # Codificación UTF-8 como en el log

    # Aplicar el icono de acuerdo al nivel de log en la columna Mensaje
    log_df['Estado'] = log_df.apply(lambda row: """<i class="text-center bi bi-check-circle-fill"></i>""" if row['Nivel'] == 'INFO' 
                                    else """<i class="text-center bi bi-x-circle-fill"></i>""" if row['Mensaje'] != row['Nivel'] 
                                    else row['Mensaje'], axis=1)
    
    log_df['Fecha'] =pd.to_datetime(log_df['Fecha'])
    log_df =log_df[log_df['Fecha'] <= datetime.now()]

    # Exportar a HTML, usando escape=False para que los caracteres HTML no sean escapados
    html_content = log_df.to_html(index=False, escape=False, classes='table table-striped table-hover')

    # Reemplazar "<table border="1" class="dataframe">" por "<table class="table table-striped table-hover">"
    html_content = html_content.replace('<table border="1" class="dataframe">', '<table class="table table-striped table-hover">')

    # Agregar Bootstrap, Bootstrap Icons y estilos CSS personalizados para centrar encabezados
    html_full = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css">
        <style>
            th {{
                text-align: center;  /* Estilo para centrar los encabezados */
            }}
        </style>
        <title>Log</title>
    </head>
    <body>
        <div class="container mt-5">
            <h2>Log de Eventos</h2>
            {html_content}
        </div>
    </body>
    </html>
    """

    # Guardar el HTML en un archivo
    with open('log.html', 'w', encoding='utf-8') as f:
        f.write(html_full)

    print("Archivo HTML con Bootstrap generado correctamente, con encabezados centrados.")
    return task

