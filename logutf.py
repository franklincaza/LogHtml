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
