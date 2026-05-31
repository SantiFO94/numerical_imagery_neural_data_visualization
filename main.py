import pandas as pd
from src.config import RAW_PATH, EP_RAW, IN_RAW, CSV_RAWS, OUT_PATH
from src.io import txt_transform_csv, load_csv_files, save_csv_file
from src.cleaning import clean, remove_electrodes
from src.features import build_features
from src.viz import avg_powers_comparison, plot_cortical_insights, plot_stimulus_comparison


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
    
    # Join dataframes for easier comparison of data
    df_complete = pd.concat(dataframes.values(), ignore_index=True) #Ignore index omite los indices de cada registro para evitar conflictos más adelante
                    
    # Process data from clean dataframes to extract frequency and temporal features
    df_features = build_features(df_complete)
    
    # Save processed data in csv files for the record
    save_csv_file(OUT_PATH, 'features.csv', df_features)

    # Data visualization to analyze features
    
    df_hemispheres = remove_electrodes(df_features, 'channel', 'PZ')
    df_lobes = remove_electrodes(df_features, 'lobe', 'Occipital')
    plot_cortical_insights(df_hemispheres, df_lobes) # Cortical activity
    
    plot_stimulus_comparison(df_features) # Pointplot showing activity by stimulus
    
    avg_powers_comparison(df_features) # Potencias medias para cada numero en cada banda
 


if __name__ == "__main__":
    main()
