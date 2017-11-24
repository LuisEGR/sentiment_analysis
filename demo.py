import indicoio

indicoio.config.api_key = '85d4520bf61a3f7e114e89725860dd53'

s = indicoio.sentiment(
    "Falta a clases, tiene cosas muy llamativas, ampliamente la recomiendo, es mas hasta repruebo y la recurso con ella", language="spanish")
print(s)
