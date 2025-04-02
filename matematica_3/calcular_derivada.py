import sympy as sp

x = sp.symbols('x')

f = 5 + 3*x**4 - sp.exp(x) + sp.sin(x**2)

derivada = sp.diff(f, x)

# Exibir o resultado
print("Derivada de f(x):", derivada)