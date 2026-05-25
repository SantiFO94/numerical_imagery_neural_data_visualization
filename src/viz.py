import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_graph(df: pd.DataFrame) -> None:
    pass

# Graph different bandwith frequencies
def plot_psd(f, Pxx):
    plt.figure(figsize=(10, 6))
    
    # Graficamos la PSD (usamos semilogy porque la potencia suele ser exponencial)
    plt.semilogy(f, Pxx, label="PSD (Welch)", color='black')
    
    # Definimos las bandas de frecuencia clásicas (ejemplo)
    bands = {
        "Delta": (0.5, 4),
        "Theta": (4, 8),
        "Alpha": (8, 13),
        "Beta": (13, 30),
        "Gamma": (30, 100)
    }
    
    # Coloreamos las bandas en el gráfico
    colors = ['#FF9999', '#99FF99', '#9999FF', '#FFCC99', '#CC99FF']
    for (name, (low, high)), color in zip(bands.items(), colors):
        plt.axvspan(low, high, color=color, alpha=0.3, label=name)
        
    plt.title("Densidad Espectral de Potencia (PSD) por Bandas")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Potencia (uV^2/Hz)")
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.2)
    
    print('----------Signal power plot----------')
    plt.show()



def plot_device_comparison(df: pd.DataFrame):

    unique_codes = df['code'].unique()
    bands = ['delta', 'theta', 'alpha', 'beta', 'gamma']
    
    for code in unique_codes:
        # Filtramos los datos para el código actual
        df_code = df[df['code'] == code]
        
        # Identificamos los dispositivos presentes en este código
        dispositivos = df_code['device'].unique()
        
        # Preparamos el gráfico
        fig, ax = plt.subplots(figsize=(10, 5))
        x = np.arange(len(bands))
        width = 0.35
        
        # Dibujamos una barra por cada dispositivo
        for i, device in enumerate(dispositivos):
            df_dev = df_code[df_code['device'] == device]
            
            # Promediamos las potencias de todas las filas para ese dispositivo
            # (asumiendo que tienes varias muestras para el mismo dispositivo/código)
            medias = [df_dev[banda].mean() for banda in bands]
            
            # Calculamos el desplazamiento para que no se encimen
            offset = (i - 0.5) * width
            ax.bar(x + offset, medias, width, label=f'Device: {device}')
            
        ax.set_title(f'Comparación de Potencia por Banda - Código: {code}')
        ax.set_xticks(x)
        ax.set_xticklabels([b.capitalize() for b in bands])
        ax.set_ylabel('Potencia Relativa Media')
        ax.legend()
        plt.grid(axis='y', linestyle='--', alpha=0.7)

    print('----------Devices comparison plots----------')
    plt.show()