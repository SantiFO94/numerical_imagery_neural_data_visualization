from pathlib import Path
import pandas as pd
from src.config import CSV_RAWS



def txt_transform_csv(path: str | Path, *input_names:  str):
    '''
    Transforms one or multiple .txt files into .csv format.

    Parses lines separated by tabs, classifying the first 5 elements as 
    metadata. The final column is treated as the recorded signal and 
    is parsed by splitting comma-separated values.
    '''
    
    print("Reading and transforming text files from input...")

    for name in input_names:
        data_rows = []
        
        output_name = name.replace('.txt', '.csv')
        output_path = path / output_name
        
        # Check if file already exists to avoid unnecessary transformations
        if output_path.exists():
            print(f"The file {output_name} already exists. Avoiding transformation.")
            CSV_RAWS.append(output_name)

            continue
        
        print("Transforming file:", name)

        with open(path / name, "r") as file:
            for i, registry in enumerate(file):
                if i >= 5000: # Only read 5000 rows
                    break
                # Separar por tabulación cada línea
                parts = registry.split("\t")

                # First 5 elements are metadata
                metadata = parts[:6]

                # Final element corresponds to the EEG signal
                signal = parts[6].split(",")

                # Create a dictionary for each row
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
        
        print(f'----------File {name} transformed correctly----------')
        print(df.head())
                
        df.to_csv(output_path, index=False)
        
        CSV_RAWS.append(output_name)
    
    print('.csv files names:', CSV_RAWS)
        
def load_csv_files(path: str | Path, input_names: list[str]):
    '''Load several CSV files into DataFrames'''

    dataframes = {}
    
    for name in input_names:
        dataframes[name] = pd.read_csv(path / name)
        print(f'----------Loaded dataframe {name}----------')
        print(dataframes[name].head())

    return dataframes

def save_csv_file(path: str | Path, name:  str, df, replace_symbol: str = None, output_suffix: str = None):

    output_name = name
    
    if replace_symbol and output_suffix:
        output_name = name.replace(replace_symbol, output_suffix)
    
    print(f'----------Saving file {output_name}----------')
    
    df.to_csv(path / output_name, index=False)
    
    print(f'----------File {output_name} saved correctly----------')

