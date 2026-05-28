import pandas as pd
import numpy as np
from scipy.signal import welch

def build_features(df: pd.DataFrame) -> pd.DataFrame:
        
        df = df.copy()
        print('----------Start extracting features from raw EEG data----------')

        # Temporal features
        df['signal_mean'] = df['signal'].apply(np.mean)
        df['signal_variance'] = df['signal'].apply(np.var)
        df['signal_power'] = df['signal'].apply(lambda x: np.ptp(x))
        
        # Frequency features
        bands = {'delta': (0.5, 4), 'theta': (4, 8), 'alpha': (8, 12), 'beta': (13, 30), 'gamma': (30, 40)}
        for band_name, (low, high) in bands.items():
                
                print(f'----------Calculating bandwith between frequencies {low} and {high}----------')

                df[band_name] = df['signal'].apply(lambda s: bandpower(s, low, high))
                
        # df['delta'] = bandpower(df['signal'], 0.5, 4)
        # df["theta"] = bandpower(df['signal'], 4, 8)
        # df["alpha"] = bandpower(df['signal'], 8, 12)
        # df["beta"] = bandpower(df['signal'], 13, 30)
        # df["gamma"] = bandpower(df['signal'], 30, 40)

        # Remove raw signal column 
        df = df.drop('signal')
        
        print('----------Finished extracting features from raw EEG data----------')
        df.head()
    

def bandpower(signal, low, high):

        np_signal = np.array(signal)
        # Extract power (pxx) for each frequency (f)
        f, pxx = welch(np_signal, fs=128, nperseg=min(128, len(np_signal)))
        
        # Create filter for a frequency range
        idx = np.logical_and(f >= low, f <= high)
        
        # Calculate bandwith absolute power
        band_power = np.sum(pxx[idx])
        
        # Calculate total power of the signal
        total_power = np.sum(pxx)
        
        # Calculate relative power of the specified frequency range
        return band_power / (total_power + 1e-10) # Add small number to avoid division by zero error