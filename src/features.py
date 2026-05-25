import pandas as pd
import numpy as np

def build_features(df: pd.DataFrame) -> pd.DataFrame:
        
        df = df.copy()
        
        # Temporal features
        df['signal_mean'] = np.mean(df['signal'])
        df['signal_variance'] = np.var(df['signal'])
        df['signal_power'] = np.ptp(df['signal'])
        
        # Frequency features
        df['delta'] = bandpower(df['signal'], 0.5, 4)
        df["theta"] = bandpower(df['signal'], 4, 8)
        df["alpha"] = bandpower(df['signal'], 8, 12)
        df["beta"] = bandpower(df['signal'], 13, 30)
        df["gamma"] = bandpower(df['signal'], 30, 40)

        # Remove raw signal column 
        df.drop('signal')
        
        print('----------Extracted features from raw EEG data----------')
        df.head()
    

def bandpower(signal, low, high):
        # Extract power (pxx) for each frequency (f)
        f, pxx = signal.welch(signal, fs=128, nperseg=min(128, len(signal)))
        
        # Calculate total power of the signal
        total_power = np.sum(pxx)
        
        # Create filter for a frequency range
        idx = np.logical_and(f >= low, f <= high)
        
        # Calculate relative power of the specified frequency range
        return np.sum(pxx[idx]) / (total_power + 1e-10) # Add small number to avoid division by zero error