import numpy as np
import matplotlib.pyplot as plt

# Dados
anos = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
populacao = np.array([2502557, 2501576, 2523794, 2501576, 2512070,
                      2521564, 2530701, 2315560, 2315560, 2315560])

# Ajuste polinomial de grau 2
coeficientes = np.polyfit(anos, populacao, 2)
polinomio = np.poly1d(coeficientes)

# Geração de valores para a curva ajustada
anos_fit = np.linspace(2015, 2024, 100)
pop_fit = polinomio(anos_fit)

# Plotagem
plt.figure(figsize=(10, 6))
plt.scatter(anos, populacao, color='blue', label='Dados Reais')
plt.plot(anos_fit, pop_fit, color='red', label='Ajuste Polinomial (Grau 2)')
plt.title('População de Belo Horizonte (2015–2024)')
plt.xlabel('Ano')
plt.ylabel('População')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
