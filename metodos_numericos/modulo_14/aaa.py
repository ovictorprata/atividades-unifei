import math
import pandas as pd

# Função a integrar
def f(x):
    return math.exp(x)

# Limites do intervalo
a, b = 0.0, 1.0

# Número de subintervalos para os métodos compostos
n = 2

# Integral exata
J_exact = math.e - 1

# 1) Trapézio simples
T_simple = (b - a) / 2 * (f(a) + f(b))

# 2) Trapézio composto
h = (b - a) / n
xs = [a + i * h for i in range(n + 1)]
T_comp = h * (f(xs[0]) / 2
              + sum(f(x) for x in xs[1:-1])
              + f(xs[-1]) / 2)

# 3) Simpson 1/3 (n deve ser par)
S = h / 3 * (f(xs[0]) + 4 * sum(f(xs[i]) for i in range(1, n, 2)) + f(xs[-1]))

# Erros
errors_abs = [abs(T_simple - J_exact),
              abs(T_comp   - J_exact),
              abs(S         - J_exact)]
errors_pct = [err / J_exact * 100 for err in errors_abs]

# Monta o DataFrame
df = pd.DataFrame({
    'Método': ['Trapézio Simples', 'Trapézio Composta (n=2)', 'Simpson 1/3 (n=2)'],
    'Aproximação': [T_simple, T_comp, S],
    'Erro Absoluto': errors_abs,
    'Erro Percentual (%)': errors_pct
})

# Exibe resultados
print(df.to_string(index=False))
print(f"\nValor exato de ∫₀¹ eˣ dx = {J_exact:.6f}")
