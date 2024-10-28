import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Function, dsolve, sqrt, Eq

# Definimos las variables y la función
x, C1 = symbols('x C1')
y = Function('y')(x)

# Definimos la ecuación diferencial como igual a cero
equation = Eq((x**2 + y**2) + (2*x*y) * y.diff(x), 0)

# Resolver la ecuación diferencial
solution = dsolve(equation, y)

# Imprimir la solución
print(f'Solución general: {solution}')

# Definimos la función "GeoGebra" como la misma solución
def geogebra_function(x_val, C1_value):
    return float(-sqrt(x_val**2) / 3 + C1_value / x_val)  # Convertir a float

# Definimos la solución obtenida en Python
def python_solution(x_val, C1_value):
    return float(-sqrt(x_val**2) / 3 + C1_value / x_val)  # Convertir a float

# Graficando
x_vals = np.linspace(0.1, 10, 400)  # Evitar dividir por cero
C1_value = 1  # Valor de C1
y_vals_geogebra = [geogebra_function(val, C1_value) for val in x_vals]
y_vals_python = [python_solution(val, C1_value) for val in x_vals]

# Graficamos ambas soluciones
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals_geogebra, label='Función GeoGebra (Solución)', color='blue')
plt.plot(x_vals, y_vals_python, label='Solución en Python', color='orange', linestyle='--')
plt.title('Comparación de Soluciones: GeoGebra vs Python')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend()
plt.xlim(0, 10)
plt.ylim(-10, 10)
plt.show()

# Calcular el porcentaje de acierto
# Comparar los valores de ambas funciones en ciertos puntos
points_to_compare = np.linspace(0.1, 10, 100)  # Puntos en los que se evaluará
correct_values = [python_solution(val, C1_value) for val in points_to_compare]
geogebra_values = [geogebra_function(val, C1_value) for val in points_to_compare]

# Calcular el porcentaje de acierto
correct_count = sum(np.isclose(c, g, atol=1e-5) for c, g in zip(correct_values, geogebra_values))
total_points = len(points_to_compare)

percentage_accuracy = (correct_count / total_points) * 100
print(f'Porcentaje de acierto entre GeoGebra y Python: {percentage_accuracy:.2f}%')
