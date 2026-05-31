import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.constants import bands
from src.config import GRAPHS


def plot_cortical_insights(df_hemispheres: pd.DataFrame, df_lobes: pd.DataFrame):
    """
    Generates graphs representing activity by different cortical areas
    """

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Graph 1: Hemispheric ativation.
    # median used to avoid outliers in signal power overflowing the visualization
    sns.barplot(
            data=df_hemispheres, 
            x='hemisphere', 
            y='signal_power', 
            hue='device', 
            ax=axes[0],
            palette='Set2',
            estimator=np.median,
            errorbar=('ci', 95),
            capsize=0.1
    )
    
    axes[0].set_title('Hemispheric activity')
    axes[0].set_xlabel('Hemisphere', fontsize=12)
    axes[0].set_ylabel('Median Power', fontsize=12)
    
    # Graph 2: Cortical lobes
    sns.barplot(
        data=df_lobes, 
        x='lobe', 
        y='signal_power', 
        hue='device', 
        ax=axes[1],
        palette='Set2',
        estimator=np.median,
        errorbar=('ci', 95),
        capsize=0.1
    )
    
    axes[1].set_title('Cortical lobes activity')
    axes[1].set_xlabel('Cortical lobe', fontsize=12)
    axes[1].set_ylabel('Potencia Mediana (Signal Power)', fontsize=12)
    
    plt.suptitle('Insights of hemispheric and cortical activity', fontsize=16, fontweight='bold')
    plt.tight_layout()
    
    plt.savefig(GRAPHS / "cortical_activity.png", bbox_inches='tight')

    plt.show()
    
    
def plot_stimulus_comparison(df: pd.DataFrame):
    """
    Visualization of differences of activity power among different stimulus
    """
    plt.figure(figsize=(12, 6))
    
    sns.pointplot(
        data=df,
        x='code',
        y='signal_power',
        hue='device',
        palette='viridis',
        estimator=np.median,
        errorbar=('ci', 95),
        capsize=0.05,
        dodge=True 
    )
    
    plt.title('Comparación de Activación por Estímulo Pensado (0-9)', fontsize=15)
    plt.xlabel('Número Pensado (Code)', fontsize=12)
    plt.ylabel('Potencia Mediana (Signal Power)', fontsize=12)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(GRAPHS / "stimulus_comparison.png", bbox_inches='tight')
    
    plt.show()
    
def avg_powers_comparison(df: pd.DataFrame):
    
    # Transformamos el DataFrame al formato "long" (tidy data)
    # Esto coloca todas las bandas en una sola columna para facilitar la agrupación
    df_long = df.melt(
        id_vars=['code', 'device'], 
        value_vars=bands, 
        var_name='Band', 
        value_name='Power'
    )
    
    # Creamos el gráfico (Faceting por código/número)
    # 'col=code' creará un gráfico distinto para cada número (0, 1, 2...)
    catplot = sns.catplot(
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
    
    catplot.set_titles("Pensando en numero: {col_name}")
    catplot.set_axis_labels("Banda de frecuencia", "Potencia Media")
    plt.subplots_adjust(top=0.85)
    catplot.fig.suptitle('Potencia Media por Banda y Código (Número)', fontsize=16)
    plt.savefig(GRAPHS / "power_comparison.png", bbox_inches='tight')

    plt.show()

    
# Graph different bandwith frequencies
def plot_psd(f, Pxx):
    '''Show spectral density power for the different bandwiths'''
    plt.figure(figsize=(10, 6))
    
    # Graficamos la PSD (usamos semilogy porque la potencia suele ser exponencial)
    plt.semilogy(f, Pxx, label="PSD (Welch)", color='black')
    
    # Definimos las bandas de frecuencia clásicas (ejemplo)
    bands_frequency_ranges = {
        "Delta": (0.5, 4),
        "Theta": (4, 8),
        "Alpha": (8, 13),
        "Beta": (13, 30),
        "Gamma": (30, 100)
    }
    
    # Coloreamos las bandas en el gráfico
    colors = ['#FF9999', '#99FF99', '#9999FF', '#FFCC99', '#CC99FF']
    for (name, (low, high)), color in zip(bands_frequency_ranges.items(), colors):
        plt.axvspan(low, high, color=color, alpha=0.3, label=name)
        
    plt.title("Densidad Espectral de Potencia (PSD) por Bandas")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Potencia (uV^2/Hz)")
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.2)
    print('----------Signal power plot----------')
    plt.show()
