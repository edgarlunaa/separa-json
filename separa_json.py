import json

def separa_json(archivo_json):
    f = open(archivo_json, 'r')
    text = f.readline()
    f.close()
    text = text[4:]
    busca_corchete = text.find('[')
    i = 0
    while busca_corchete != -1:
        nombre_grupo = text[1:text.find('"',1)]
        nombre_grupo = nombre_grupo.replace("/", "-")
        nombre_grupo = nombre_grupo.replace("con", "cn")
        algun_json = text[busca_corchete:]
        busca_cierre = algun_json.find("]")
        algun_json = algun_json[:busca_cierre + 1]
        
        nombre_archivo_json = nombre_grupo + ' ' + archivo_json
        with open(nombre_archivo_json, 'w') as j:
            j.write(algun_json)
        
        with open("nombres de archivos.txt", 'a') as archivo_nombres:
            archivo_nombres.write(nombre_archivo_json + '\n')

        busca_cierre = text.find("]")
        text = text[busca_cierre + 2:]
        busca_corchete = text.find('[')
        i += 1