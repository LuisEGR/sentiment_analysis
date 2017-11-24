import json
import codecs
import glob

files = glob.glob("sentimientos*_*.json");
# print(files)


for file in files:
    clasifications = json.load(codecs.open(file, 'r', 'utf-8-sig'))
    for c in clasifications:
        sentim_id = int(round((c["happiness"] / 2) * 10, 0))
        if c["happiness"] != 0:
            print('UPDATE evaluacion SET sentiment_id = ' +
                  str(sentim_id) + ' WHERE id = ' + str(c["id"]) + ';')

# files = 
# clasifications = json.load(codecs.open(
    # 'comentarios23112017.json', 'r', 'utf-8-sig'))
