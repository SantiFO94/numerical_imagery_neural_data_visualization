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

def get_hemisphere(channel):
    '''Odd channels correspond to left hemisphere, 
    even channels correspond to right hemisphere, 
    PZ es central'''
    
    if channel == 'PZ': return 'Central'
    
    num = int(''.join(filter(str.isdigit, channel)))
    
    return 'Left' if num % 2 != 0 else 'Right'

def get_lobe(channel):
    '''Cortical lobe mapping based on electrode naming'''
    
    mapping = {'AF': 'Frontal', 'F': 'Frontal', 'FC': 'Frontal', 
               'T': 'Temporal', 'P': 'Parietal', 'O': 'Occipital'}
    
    for key, lobe in mapping.items():
        if channel.startswith(key): return lobe
    return 'Other'