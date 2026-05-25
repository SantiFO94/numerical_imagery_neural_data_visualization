import pandas as pd
from src.config import RAW_PATH, EP_RAW, IN_RAW, CSV_RAWS, OUT_PATH
from src.io import txt_transform_csv, load_csv_files, save_csv_file
from src.cleaning import clean
from src.features import build_features
from src.utils import assert_columns
from src.viz import plot_graph


def main():
    # Transform files from .txt to .csv
    txt_transform_csv(RAW_PATH, EP_RAW, IN_RAW) # Select Emotiv EPOC and Emotiv Insight for comparisons between devices (128hz, coincident channels) 
    
    # Load new .csv files to dataframes in a dictionary for their manipulation
    dataframes = load_csv_files(RAW_PATH, CSV_RAWS)
   
    # Clean dataframes for better feature extraction
    for file_name, df in dataframes.items():
        dataframes[file_name] = clean(df)
    
    # Save clean dataframes    
    for name, df in dataframes.items():
        save_csv_file(OUT_PATH, name, df, replace_symbol= '.', output_suffix = '_clean.')
    
    df_complete = pd.concat(dataframes.values(), ignore_index=True) #Ignore index omite los indices de cada registro para evitar conflictos más adelante

    df_features = build_features(df_complete)
    
    save_csv_file(OUT_PATH, 'features', df_features)

    # assert_columns(df, ['column_1', 'column_2'])

    # Llamada a la función
    # plot_psd(f, Pxx)
    # plot_device_comparison
    
    # OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # df.to_csv(OUT_PATH, index=False)
    # print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    main()
