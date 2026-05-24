from pathlib import Path
import pandas as pd
from config import CSV_RAWS



def txt_transform_csv(path: str | Path, *input_names:  str):
    '''
    Transforma uno o varios archivos .txt a archivos .csv.
    
    Separa todas las columnas separadas por una tabulación y
    clasifica las 5 primeras como metadatos del registro.  
    La última columna se considera la señal registrada y 
    se separa cada registro por comas.
    '''
    
    print("Leyendo y estructurando el dataset de señales...")

    for name in input_names:
        data_rows = []

        with open(path / name, "r") as file:
            for registry in file:
                # Separar por comas cada línea
                parts = registry.split("\t")

                # Los primeros 6 elementos son los metadatos
                metadata = parts[:6]

                # El resto de la línea es la señal neuronal
                signal = parts[6].split(",")

                # Creamos un diccionario limpio por cada fila
                row = {
                    "id": metadata[0],
                    "event": metadata[1],
                    "device": metadata[2],
                    "channel": metadata[3],
                    "code": metadata[4],
                    "size": metadata[5],
                    "signal": signal,
                }
                
                data_rows.append(row)

        df = pd.DataFrame(data_rows)
        output_name = name.replace('.txt','.csv')
        
        df.to_csv(path / output_name, index=False)
        
        CSV_RAWS.append(output_name)
        
def load_csv(path: str | Path, *input_names:  str):
    """Load several CSV files into DataFrames."""

    dataframes = []
    
    for name in input_names:
        dataframes.append({name, load_csv(path / name)})
    
    return dataframes


def load_csv(path: str | Path):
    """Load a CSV file into a DataFrame."""
    
    return pd.read_csv(path)
