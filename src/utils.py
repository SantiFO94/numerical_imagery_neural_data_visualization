import pandas as pd

def assert_columns(df: pd.DataFrame, required: list[str]) -> None:
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f'Missing columns: {missing}')

def parse_strings_list(s):
    if isinstance(s, str):
        # Remove brackets and string formatting symbols
        s = s.replace('[', '').replace(']', '').replace('\\n', '').replace('"', '').replace("'", '')

        # Convert to float if not empty
        return [float(x) for x in s.split(',') if x.strip()]
    return s