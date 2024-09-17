# La librería logging de Python
La librería logging de Python es una herramienta poderosa para generar y controlar mensajes de log en tus aplicaciones. Te permite registrar eventos que ocurren mientras se ejecuta un programa, lo que es útil para la depuración, monitoreo, y auditoría. Puedes personalizar los mensajes de log y elegir qué tan detallados serán utilizando diferentes niveles de severidad.

Niveles de Log en logging
Existen varios niveles que indican la gravedad de los eventos que se están registrando:

DEBUG: Información detallada, típicamente de interés solo cuando se diagnostican problemas.
INFO: Confirmación de que las cosas funcionan como se esperaba.
WARNING: Indicación de que algo inesperado sucedió o indicación de un problema en el futuro cercano (por ejemplo, "disco lleno").
ERROR: Debido a un problema más grave, el software no puede realizar alguna función.
CRITICAL: Error muy grave, el programa podría no ser capaz de continuar ejecutándose.
Formatos en logging
Uno de los aspectos más importantes de logging es la capacidad de personalizar los mensajes que genera, utilizando Formatter. El formato de los logs puede incluir información como la fecha, el nivel de severidad, el nombre del archivo, y el mensaje en sí. Aquí están algunos de los formatos más comunes:
```
%(levelname)s: El nivel de severidad del log (DEBUG, INFO, WARNING, ERROR, CRITICAL).
%(asctime)s: El timestamp cuando se registró el log.
%(message)s: El mensaje de log que se pasa a las funciones logger.debug(), logger.info(), etc.
%(name)s: El nombre del logger.
%(filename)s: El nombre del archivo en el que se generó el log.
%(lineno)d: El número de línea del archivo donde se generó el log.
%(funcName)s: El nombre de la función desde donde se llama el log.
%(module)s: El nombre del módulo (el archivo sin la extensión .py).
%(threadName)s: El nombre del hilo en el que se generó el log.
%(process)d: El ID del proceso desde donde se generó el log.
```
Ejemplo de configuración básica
```python
Copiar código
import logging

# Configurar el logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Crear logger
logger = logging.getLogger(__name__)

# Mensajes de log con diferentes niveles
logger.debug("Este es un mensaje de depuración")
logger.info("Este es un mensaje informativo")
logger.warning("Este es una advertencia")
logger.error("Este es un mensaje de error")
logger.critical("Este es un mensaje crítico")
```
En este ejemplo, se utiliza el formato
```
'%(asctime)s - %(name)s - %(levelname)s - %(message)s', que incluye la fecha y hora, el nombre del logger, el nivel del log, y el mensaje en sí.
```
Personalización avanzada
Puedes personalizar aún más utilizando Formatter y agregar tus propios Handlers para enviar los logs a diferentes destinos, como archivos o la consola.
```
python
Copiar código
import logging

# Crear logger
logger = logging.getLogger('mi_logger_personalizado')
logger.setLevel(logging.DEBUG)

# Crear un handler para escribir en archivo
file_handler = logging.FileHandler('mi_log.log')
file_handler.setLevel(logging.WARNING)

# Crear un handler para imprimir en consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Definir el formato
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Añadir handlers al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Mensajes de ejemplo
logger.debug("Mensaje de depuración")
logger.info("Mensaje informativo")
logger.warning("Advertencia")
logger.error("Error")
logger.critical("Crítico")
```
En este ejemplo, se configuran dos Handlers: uno que escribe logs en un archivo y otro que los imprime en la consola.

Formatos personalizados
Puedes crear tus propios formatos utilizando los elementos que mencioné antes, o combinarlos para adaptarlos a tus necesidades:

```python
Copiar código
formatter = logging.Formatter('%(levelname)s at %(asctime)s in %(module)s: %(message)s')
```
Este formato mostrará el nivel de log, seguido de la hora, el módulo desde el cual se generó el log y el mensaje.
