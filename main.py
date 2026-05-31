import pandas as pd
from src.config import RAW_PATH, EP_RAW, IN_RAW, CSV_RAWS, OUT_PATH
from src.io import txt_transform_csv, load_csv_files, save_csv_file
from src.cleaning import clean
from src.features import build_features
from src.viz import avg_powers_comparison, plot_power_by_band_and_event, plot_cortical_insights, plot_stimulus_comparison


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
    
    save_csv_file(OUT_PATH, 'features.csv', df_features)

    plot_cortical_insights(df_features) # Cortical activity
    plot_stimulus_comparison(df_features) # Pointplot showing activity by stimulus
    avg_powers_comparison(df_features) # Potencias medias para cada numero en cada banda
    plot_power_by_band_and_event(df_features) # Barplot with signal power by stimulus and device in each bandwith

    # plot_device_comparison(df_features)
    



if __name__ == "__main__":
    main()
