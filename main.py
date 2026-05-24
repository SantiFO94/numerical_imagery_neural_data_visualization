from src.config import RAW_PATH, EP_RAW, IN_RAW, MU_RAW, MW_RAW, CSV_RAWS, OUT_PATH
from src.io import txt_transform_csv, load_csv
from src.cleaning import clean
from src.features import build_features
from src.utils import assert_columns
from src.viz import plot_graph


def main():
    #Transformación de archivos .txt a .csv
    txt_transform_csv(RAW_PATH, EP_RAW, IN_RAW, MU_RAW, MW_RAW)
    
    #Carga de archivos .csv a dataframes
    df = load_csv(RAW_PATH, CSV_RAWS)
    df.head()
    # df = clean(df)
    # df = build_features(df)
    # assert_columns(df, ['column_1', 'column_2'])

    # plot_graph(df)

    # OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # df.to_csv(OUT_PATH, index=False)
    # print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    main()
