import os
import json
from pathlib import Path
from pathlib import Path
import csv

def readJSON(path):
	with open(path, "r", encoding='utf8') as json_file:
		return json.load(json_file)

def writeCSV(path,data,demiliter):
	with open(pathCsv, 'w', newline='',encoding='utf8') as csv_file:
		writer = csv.writer(csv_file, delimiter =demiliter,quotechar =',',quoting=csv.QUOTE_MINIMAL)
		data = list(data.values())[0]
		titulos = list(data[0].keys())
		titulos.append("Total")
		writer.writerow(titulos)
		totalFinal = 0
		for x in data:
			valores = list(x.values())
			total = float(valores[3]) * float(valores[4])
			totalFinal+=total
			valores.append(total)
			writer.writerow(valores)
		writer.writerow(["Total","","","","",totalFinal])      



diretorio = os.path.abspath(os.path.dirname(__file__))
arquivoJson = Path(diretorio + "/json/exemplo/shopping.json")
data = readJSON(arquivoJson)
pathCsv = Path(diretorio + "/gerados/" + arquivoJson.name.split(".")[0] + ".csv")
writeCSV(pathCsv,data,"|")






