import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def avg_powers_comparison(df: pd.DataFrame):
    # 1. Definimos las bandas según tu configuración de features.py
    bands = ['delta', 'theta', 'alpha', 'beta', 'gamma']
    
    # 2. Transformamos el DataFrame al formato "long" (tidy data)
    # Esto coloca todas las bandas en una sola columna para facilitar la agrupación
    df_long = df.melt(
        id_vars=['code', 'device'], 
        value_vars=bands, 
        var_name='Band', 
        value_name='Power'
    )
    
    # 3. Creamos el gráfico (Faceting por código/número)
    # 'col=code' creará un gráfico distinto para cada número (0, 1, 2...)
    g = sns.catplot(
        data=df_long, 
        kind='bar',
        x='Band', 
        y='Power', 
        hue='device', 
        col='code', 
        col_wrap=4,  # Ajusta según cuántos códigos tengas
        palette='viridis',
        height=3.5, 
        aspect=1.0,
        sharey=True # Mantenemos la misma escala Y para comparar fácilmente entre códigos
    )
    
    g.set_titles("Pensando en numero: {col_name}")
    g.set_axis_labels("Banda de frecuencia", "Potencia Media")
    plt.subplots_adjust(top=0.85)
    g.fig.suptitle('Potencia Media por Banda y Código (Número)', fontsize=16)
    
    plt.show()
    
def plot_event_comparison(df: pd.DataFrame):
    """
    Generates a comparative bar chart of signal_power 
    by event (-1 - 9) and device (IN/EP).
    """
    # Set the plotting theme
    sns.set_theme(style="whitegrid")
    
    # Create the figure
    plt.figure(figsize=(12, 6))
    
    # Barplot automatically groups by 'event' on the X axis 
    # and uses 'hue' to separate by device
    chart = sns.barplot(
        data=df, 
        x='event', 
        y='signal_power', 
        hue='device', 
        palette='viridis'
    )
    
    plt.title('Signal Power Comparison by Event and Device', fontsize=15)
    plt.xlabel('Event', fontsize=12)
    plt.ylabel('Signal Power', fontsize=12)
    plt.legend(title='Device')
    
    plt.tight_layout()
    plt.show()

def plot_power_by_band_and_event(df: pd.DataFrame):
    """
    Generates comparative charts of mean power per frequency band,
    grouping by event and device.
    """
    # 1. Define frequency bands based on configuration
    bands = ['delta', 'theta', 'alpha', 'beta', 'gamma']
    
    # 2. Transform the DataFrame to long format (tidy data)
    # This places all bands into a single column to facilitate grouping
    df_long = df.melt(
        id_vars=['event', 'device'], 
        value_vars=bands, 
        var_name='Band', 
        value_name='Power'
    )
    
    # 3. Create the plot (Faceting by event)
    # Seaborn automatically creates a subplot for each 'event'
    g = sns.catplot(
        data=df_long, 
        kind='bar',
        x='Band', 
        y='Power', 
        hue='device', 
        col='event', 
        col_wrap=5,  # Organize events in rows of 5
        palette='muted',
        height=3, 
        aspect=1.2
    )
    
    g.set_titles("Event: {col_name}")
    g.set_axis_labels("Frequency Band", "Mean Power")
    plt.subplots_adjust(top=0.9)
    g.fig.suptitle('Mean Power per Band by Event and Device', fontsize=16)
    
    plt.show()
    
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