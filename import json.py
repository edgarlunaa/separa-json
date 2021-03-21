import glob
import shutil
import json 
import pandas as pd 

#Rutas de ARchivos JSON a procesar y de backup luego de procesados
dir_origen = r'D:\DESARROLLO\EMPLEO\separa-json\archivos'
dir_back = r'D:\DESARROLLO\EMPLEO\separa-json\archivos\backup'

lista_data = []
archivos_json_emprendedores = glob.glob(dir_origen + r"\*.JSON")
for filename in archivos_json_emprendedores:
    with open(filename, encoding='utf-8-sig', errors='ignore') as f: #IMPORTANTE EL utf-8-sig 
        d = json.load(f, strict=False)
    for key in d.keys():
        df_json = pd.DataFrame.from_dict(d[key]) #Listo to DF
        lista_data.append(df_json)
    df_result = pd.concat(lista_data, axis=1)
    df_result.to_csv("resultado.csv", mode='a', index=False, header=None) #PANDAS AGREGA A UN ARCHIVO CSV MODE "A"
    archivo = filename[(filename.rfind('\\')):]
    shutil.move(filename, str(dir_back  +  archivo))
pass