import json
import codecs

import indicoio

indicoio.config.api_key = '85d4520bf61a3f7e114e89725860dd53'

opiniones = json.load(codecs.open('comentarios23112017.json', 'r', 'utf-8-sig'))
data_result = []
print("Analizando...")
for opinion in opiniones[1000:1831]:
    sentimiento = 0
    if opinion['comentario'] and opinion['comentario'].strip() != "":
        sentimiento = indicoio.sentiment(
            opinion['comentario'], language="spanish")
    # print("id: " + str(opinion['id']))
    
    print(str(sentimiento) + ", " + str(opinion['id']))
    data_result.append({
        "id": opinion['id'],
        "happiness": sentimiento
    })


with codecs.open('sentimientos23112017_second2k_p2.json', 'w', 'utf-8') as outfile:
    json.dump(data_result, outfile)
