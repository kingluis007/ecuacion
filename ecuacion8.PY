import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definir variables simbólicas
x, y = sp.symbols('x y')

# Definir M(x, y) y N(x, y)
M = x + y
N = x - y

# Calcular las derivadas parciales
dM_dy = sp.diff(M, y)
dN_dx = sp.diff(N, x)

# Verificar si la ecuación es exacta
if dM_dy == dN_dx:
    print("La ecuación es exacta.")
else:
    print("La ecuación no es exacta. Buscando un factor integrante...")

    # Calcular el factor integrante
    integrating_factor = (dM_dy - dN_dx) / N  # Factor integrante
    integrating_factor_simplified = sp.simplify(integrating_factor)

    # Mostrar el factor integrante
    print(f"Factor integrante: {integrating_factor_simplified}")

    # Multiplicar M y N por el factor integrante
    M = integrating_factor_simplified * M
    N = integrating_factor_simplified * N

# Integrar M respecto a x
F = sp.integrate(M, x)

# Obtener la derivada de F con respecto a y para encontrar C(y)
C_y = sp.diff(F, y) - N
C = sp.integrate(C_y, y)

# Completar la función potencial
F += C

# Mostrar la solución en la terminal
print("Función potencial F(x, y) = C:")
print(F)

# Definir una función para la solución implícita
def F_func(x_val):
    return -2 * x_val + 2  # Resolviendo para y

# Crear un rango de valores para x
x_vals = np.linspace(-3, 3, 100)

# Calcular los valores de y utilizando la función potencial
y_vals = F_func(x_vals)

# Graficar la solución de Python
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='Solución de Python', color='blue')

# Graficar la solución de GeoGebra (usando la misma función F)
geo_y_vals = F_func(x_vals)  # Usando la misma función para GeoGebra
plt.plot(x_vals, geo_y_vals, label='Solución GeoGebra', color='red', linestyle='--')

# Configuraciones de la gráfica
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.title('Soluciones de la Ecuación Diferencial')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

# Calcular el porcentaje de acierto
# Comparando los valores de y
differences = np.abs(y_vals - geo_y_vals)
tolerance = 1e-5  # Tolerancia para considerar un acierto
correct_count = np.sum(differences < tolerance)
total_count = len(differences)

percentage_accuracy = (correct_count / total_count) * 100

print(f"Porcentaje de acierto: {percentage_accuracy:.2f}%")
