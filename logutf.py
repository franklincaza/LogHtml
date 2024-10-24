import logging
# Configurar el logger con codificación UTF-8
logging.basicConfig(
    filename='log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s - %(lineno)d - %(filename)s',
    encoding='utf-8'  # Especifica la codificación
)

def log(info):
    logging.info(str(info))
    print(str(info))


def Documentacion(info):
    # Obtener la fecha y hora actual en el formato especificado
    fecha_hora = datetime.now().strftime('%d/%m/%Y %I:%M %p')
    
    # Crear el mensaje con fecha, hora y el comentario
    mensaje = f"{fecha_hora} {str(info)}"
    
    # Registrar el mensaje en el log
    logging.info(info)
    
    # Imprimir el mensaje en la consola
    print(mensaje)
