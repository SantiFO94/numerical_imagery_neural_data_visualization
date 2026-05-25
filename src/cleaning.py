import pandas as pd
import ast

def clean(df_input: pd.DataFrame) -> pd.DataFrame:
    '''
    Clean the dataset:
    - Remove whitespaces
    - Fix numerical metadata types
    - Drop invalid registries
    - Convert signal to float values
    '''

    # --- Copy to avoid mutating original df ---
    df = df_input.copy()

    # --- Basic validation ---
    if df.empty:
        raise ValueError("Input DataFrame is empty")

    # --- Remove duplicates ---
    df = df.drop_duplicates()
    
    # --- 1. Remove leading and trailing whitespaces ---
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip()
        
    # --- 2. Fix columns types for further validations ---
    numeric_cols = ['event', 'code', 'size']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    print(df['signal'].iloc[0][-1])

    if 'signal' in df.columns:
        df['signal'] = df['signal'].apply(ast.literal_eval)

        
    # --- 3. Remove registries with invalid data
    # Drop registries with null values in metadata
    df = df.dropna(subset=numeric_cols)
        
    # Convert to integer type once invalid registries are discarded
    df[numeric_cols] = df[numeric_cols].astype(int)
    
    # Drop registries without neural signal
    df = df[len(df['signal']) > 0]

    # --- 4. Convert signal to float type list ---
    if 'signal' in df.columns:
        df['signal'] = df['signal'].apply(lambda signals: [float(x) for x in signals])
        
    print('----------Cleaned dataset----------')
    print(df.head())
    print(df.describe())
    
    return df
    