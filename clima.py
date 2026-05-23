import pandas as pd
import matplotlib.pyplot as plt
import os

def analizar_clima(ruta_csv):
    df = pd.read_csv(ruta_csv)
    
    # 1. Cálculos actuales
    media = df['Mean'].mean()
    print(f"--- REPORTE ESCENARIO A ---")
    print(f"Media anual global: {media:.2f}")
    
    # 2. Obtener mínima y máxima con sus respectivos años
    fila_min = df.loc[df['Mean'].idxmin()]
    fila_max = df.loc[df['Mean'].idxmax()]
    
    temp_min = fila_min['Mean']
    anio_min = int(fila_min['Year'])
    
    temp_max = fila_max['Mean']
    anio_max = int(fila_max['Year'])
    
    # Asegurar que las carpetas existan
    os.makedirs('resultados', exist_ok=True)
    
    # 3. Guardar los extremos en el archivo .txt
    ruta_txt = 'resultados/registro_temperaturas.txt'
    with open(ruta_txt, 'w', encoding='utf-8') as archivo:
        archivo.write("=== REGISTRO HISTÓRICO DE EXTREMOS CLIMÁTICOS ===\n")
        archivo.write(f"Temperatura Mínima Histórica: {temp_min} (Año: {anio_min})\n")
        archivo.write(f"Temperatura Máxima Histórica: {temp_max} (Año: {anio_max})\n")
    
    print(f"Registro de temperaturas guardado en: {ruta_txt}")
    
    # 4. Gráfico
    plt.plot(df['Year'], df['Mean'])
    plt.title('Tendencia Climática')
    plt.savefig('resultados/grafico_tendencia.png')
    print("Gráfico generado en /resultados")

if __name__ == "__main__":
    analizar_clima('datos/annual.csv')
