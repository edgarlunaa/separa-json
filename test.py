import json
import pandas as pd
from separa_json import separa_json

def main():
    separa_json("DATO_MOD.json")
    with open("nombres de archivos.txt", 'r') as nombres:
        for linea in nombres.readlines():
            df_json = pd.read_json(linea[:-1])
            df_json.to_excel(linea[:-1] + " Excel.xlsx")

if __name__ == '__main__':
    main()