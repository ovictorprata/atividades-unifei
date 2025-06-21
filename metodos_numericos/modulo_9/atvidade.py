import numpy as np
import matplotlib.pyplot as plt

# ----------------------
# Métodos Iterativos
# ----------------------

def gauss_jacobi(A, b, x0=None, tol=1e-10, max_iter=100):
    n = len(b)
    x = np.zeros(n) if x0 is None else x0.copy()
    iteracoes = [x.copy()]

    for _ in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        iteracoes.append(x_new.copy())
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, len(iteracoes)-1, iteracoes
        x = x_new
    return x, max_iter, iteracoes

def gauss_seidel(A, b, x0=None, tol=1e-10, max_iter=100):
    n = len(b)
    x = np.zeros(n) if x0 is None else x0.copy()
    iteracoes = [x.copy()]

    for _ in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))
            s2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - s1 - s2) / A[i][i]
        iteracoes.append(x.copy())
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, len(iteracoes)-1, iteracoes
    return x, max_iter, iteracoes

# ----------------------
# Sistema Linear
# ----------------------

A = np.array([
    [10, 2, 1],
    [2, 10, 3],
    [3, 4, 10]
], dtype=float)

b = np.array([9, 22, 34], dtype=float)

# Verificar Critério das Linhas
print("Verificação do Critério das Linhas (diagonal dominante):")
for i in range(len(A)):
    soma_linha = sum(abs(A[i][j]) for j in range(len(A)) if j != i)
    print(f"Linha {i+1}: |{A[i][i]}| > {soma_linha}? {'Sim' if abs(A[i][i]) > soma_linha else 'Não'}")

# ----------------------
# Solução Exata
# ----------------------

x_exata = np.linalg.solve(A, b)
print("\nSolução exata:", x_exata)

# ----------------------
# Aplicar Métodos
# ----------------------

x0 = np.zeros(len(b))

x_jacobi, it_jacobi, historico_jacobi = gauss_jacobi(A, b, x0)
x_seidel, it_seidel, historico_seidel = gauss_seidel(A, b, x0)

print("\nMétodo de Gauss-Jacobi:")
print("Solução aproximada:", x_jacobi)
print("Iterações:", it_jacobi)

print("\nMétodo de Gauss-Seidel:")
print("Solução aproximada:", x_seidel)
print("Iterações:", it_seidel)

# ----------------------
# Erro
# ----------------------

erro_jacobi = np.linalg.norm(x_exata - x_jacobi)
erro_seidel = np.linalg.norm(x_exata - x_seidel)

print(f"\nErro Gauss-Jacobi: {erro_jacobi:.2e}")
print(f"Erro Gauss-Seidel: {erro_seidel:.2e}")

# ----------------------
# Gráficos de Convergência
# ----------------------

def plot_convergencia(historico, titulo):
    erros = [np.linalg.norm(x - x_exata) for x in historico]
    plt.plot(erros, marker='o')
    plt.yscale('log')
    plt.xlabel('Iterações')
    plt.ylabel('Erro (norma)')
    plt.title(titulo)
    plt.grid(True)
    plt.show()

plot_convergencia(historico_jacobi, 'Convergência - Gauss-Jacobi')
plot_convergencia(historico_seidel, 'Convergência - Gauss-Seidel')
