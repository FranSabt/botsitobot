# botsitobot

Un bot de telegram para monitorear el estado de equipos ip a distancia, el bot realiza un ping al equipo, en primera instancia muestra el estado de todos los equipo, luego, solamente muestra aquellos equipos que cambien de estado.

El bot funciona por hilos, por lo cual no se detiene su ejecucion cundo se le solicita manualmente la informacion, sin embargo no funciona tomando otro nucleo del procesador, es mas parecido al async await de nodejs.

Otro aspecto importane es que la libreria parece no funcionar en equipos Windows, no probe en MacOs, por  lo que recomiendo usar Ubuntu/Debian o en su defecto usar una imagen de Docker con Python 3.11.

PD: para usar el canal de Telegram tuve que mandar un msj desde el canal y atrapar el ID ya que el que mostrabna el navegador no funcionaba.
PD2: No use acentos en README por problemas con mi equipo.
