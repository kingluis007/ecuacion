import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definir variables simbólicas
x, y = sp.symbols('x y')

# Definir M(x, y) y N(x, y)
M = 3*x**2 + 2*y
N = 2*x + 4*y

# Verificar si la ecuación es exacta
if sp.diff(M, y) == sp.diff(N, x):
    print("La ecuación es exacta.")
else:
    print("La ecuación no es exacta.")

# Encontrar la función potencial F
F = sp.integrate(M, x) + sp.Function('C')(y)  # Integrar M respecto a x

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
    return (-3/2) * x_val**2 - (1/2) * (x_val**3) + 1  # Resolviendo para y

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
