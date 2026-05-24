import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the dataset:
    - Handle null values
    - Fix data types
    - Drop unnecessary columns
    - Remove duplicates
    """
    output_suffix = "_CLEAN"

    # --- Copy to avoid mutating original df ---
    df = df.copy()
    # --- TODO limpiar todos los campos del dataset para quitar espacios en blanco antes y después de cada valor con .strip()
    # --- TODO convertir a int los valores de evento, estimulo y tamaño
    # --- TODO convertir a float los valores de las señales para poder usarlos en lso cálculos con signal = [float(x) for x in parts[6:] if x]

    # --- Basic validation ---
    if df.empty:
        raise ValueError("Input DataFrame is empty")

    # --- Handle missing values --- #TODO cambiar nombres de columnas
    if "children" in df.columns:
        df["children"] = df["children"].fillna(0)

#TODO cambiar nombres de columnas
    if "country" in df.columns:
        df["country"] = df["country"].fillna("Unknown")

#TODO cambiar nombres de columnas
    # --- Fix data types ---
    if "is_canceled" in df.columns:
        df["is_canceled"] = df["is_canceled"].astype(bool)

#TODO cambiar nombres de columnas
    # --- Drop unnecessary columns ---
    if "company" in df.columns:
        df = df.drop(columns=["company"])

    # --- Remove duplicates ---
    df = df.drop_duplicates()

#TODO aplicar filtros digitales (como un filtro pasabanda o filtros Notch para quitar el ruido de la red eléctrica de 50/60 Hz

#TODO implementar guardado de csv con datos limpios
    # replace_symbol = '.'
    # output_suffix = "_CLEAN."
    
    # for name in input_names:
    #     output_name = name.replace('.', output_suffix)
    
    # return pd.read_csv(path)

    return df
