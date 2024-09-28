import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    #1Ler os dados do arquivo CSV
    df = pd.read_csv("boilerplate-sea-level-predictor/epa-sea-level.csv")

    #2 Criar o gráfico de dispersão
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label="Original Data", color="blue", alpha=0.5)

    #3 Criar a primeira linha de melhor ajuste 
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series([i for i in range(1880, 2051)])
    sea_levels_predicted = intercept + slope * years_extended
    plt.plot(years_extended, sea_levels_predicted, label="Fit Line 1880-2050", color="red")

    #4Criar a segunda linha de melhor ajuste 
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent_extended = pd.Series([i for i in range(2000, 2051)])
    sea_levels_recent_predicted = intercept_recent + slope_recent * years_recent_extended
    plt.plot(years_recent_extended, sea_levels_recent_predicted, label="Fit Line 2000-2050", color="green")

    #5 Adicionar rótulos, título e legenda
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()

    #6 Salvar o gráfico e retornar o eixo para teste
    plt.savefig('sea_level_plot.png')
    return plt.gca()