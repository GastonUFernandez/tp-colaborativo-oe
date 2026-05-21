import pandas as pd
import matplotlib.pyplot as plt

def analizar_clima(ruta_csv):
    df = pd.read_csv(ruta_csv)
    media = df['Mean'].mean()
    print(f"--- REPORTE ESCENARIO A ---")
    print(f"Media anual: {media}")
    
    plt.plot(df['Year'], df['Mean'])
    plt.title('Tendencia Climática')
    plt.savefig('resultados/grafico_tendencia.png')
    print("Gráfico generado en /resultados")

if __name__ == "__main__":
    analizar_clima('datos/annual.csv')
