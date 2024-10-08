from flask import Flask, render_template
import pandas as pd
from datetime import datetime
import logging

app = Flask(__name__)

# Página log
@app.route("/log")  
def log():
    import warnings

    # Ignorar advertencias relacionadas con `pd.to_datetime`
    warnings.filterwarnings("ignore", message="Could not infer format")

    try:
        # Leer el archivo de log
        log_df = pd.read_csv('log.log', 
                            sep=r'\s-\s',  # Expresión regular para manejar separadores con espacios
                            header=None,   
                            names=['Fecha', 'Nivel', 'Mensaje'],  # Columnas personalizadas
                            engine='python', 
                            encoding='utf-8',  # Codificación para evitar errores
                            on_bad_lines='skip')  # Ignora líneas mal formadas
        
        # Aplicar el icono de acuerdo al nivel de log en la columna Mensaje
        log_df['Estado'] = log_df.apply(lambda row: """<i class="text-center bi bi-check-circle-fill"></i>""" 
                                        if row['Nivel'] == 'INFO' else 
                                        """<i class="text-center bi bi-x-circle-fill"></i>""" 
                                        if row['Mensaje'] != row['Nivel'] else row['Mensaje'], axis=1)
        
        # Convertir la columna 'Fecha' a formato datetime
        log_df['Fecha'] = pd.to_datetime(log_df['Fecha'], errors='coerce')  # Convierte a NaT las fechas inválidas
        log_df = log_df[log_df['Fecha'] <= datetime.now()]  # Filtra las fechas válidas

    except Exception as e:
        logging.error(f"Error al leer o procesar el archivo log.log: {e}")
        return "Error al procesar el archivo de log"

    # Exportar a HTML, sin escapar los caracteres HTML
    html_content = log_df.to_html(index=False, escape=False, classes='table table-striped table-hover', table_id='logTable')

    # Agregar Bootstrap, DataTables y el script para manejar la tabla
    html_full = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css">
        <link rel="stylesheet" href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css">
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
        
        <!-- Scripts de DataTables y jQuery -->
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
        <script>
            $(document).ready(function() {{
                $('#logTable').DataTable({{
                    "searching": true,   // Habilita la búsqueda en la tabla
                    "paging": true,      // Habilita la paginación
                    "info": true,        // Muestra información de la tabla
                    "ordering": true     // Habilita la opción de ordenar las columnas
                }});
            }});
        </script>
    </body>
    </html>
    """

    logging.info("Archivo HTML con Bootstrap y DataTables generado correctamente.")
    
    # Guardar el HTML en un archivo
    with open('templates/log.html', 'w', encoding='utf-8') as f:
        f.write(html_full)

    return render_template("log.html")

if __name__ == '__main__':
    app.run(debug=True)
