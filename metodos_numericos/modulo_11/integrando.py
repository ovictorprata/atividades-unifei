import sympy as sp

x = sp.Symbol('x')
f = x * sp.ln(x**2 + 1)

# Integral definida de 0 a 1
integral = sp.integrate(f, (x, 0, 1))

# Mostrar resultado simbólico e numérico
print("Resultado simbólico:", integral)
print("Resultado numérico:", float(integral))
