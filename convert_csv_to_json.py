import json
import csv
import os
from pathlib import Path
from pathlib import Path


def readCSV(path,delimiter):
	with open(path,"r") as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=delimiter)
		data = []
		for row in csv_reader:
			data.append(row)
	return data

def writeCSV(path,data):
	chaves = data[0]
	listJson = []
	total = 0
	for x in range(1,len(data)):
		row = data[x]
		dictJson = {}
		total+= (int(row[3]) * float(row[4]))
		for z in range(len(row)):
			dictJson[chaves[z]] = row[z]

		listJson.append(dictJson)
	dictJsonFinal = {"order":listJson,"total":total}

	
	with open(path, "w") as json_file:
	    json.dump(dictJsonFinal, json_file,ensure_ascii=False, indent=4)




diretorio = os.path.abspath(os.path.dirname(__file__))

arquivoCSV = Path(diretorio + "/csv/exemplo/shopping.csv")
print(arquivoCSV)

dataCsv = readCSV(arquivoCSV,"|")

arquivoJson = Path(diretorio + "/gerados/shopping.json")

writeCSV(arquivoJson, dataCsv)



