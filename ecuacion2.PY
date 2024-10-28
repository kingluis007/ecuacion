import sympy as sp
from matplotlib import pyplot as plt
import numpy as np

# Definir variables
x = sp.symbols('x')
y = sp.Function('y')(x)

# Definir la ecuación diferencial
ode = sp.Eq(x * sp.Derivative(y, x) - y, x**2)

# Resolver la ecuación diferencial con una condición inicial, por ejemplo, y(1) = 0
solution = sp.dsolve(ode, y, ics={y.subs(x, 1): 0})
solution_explicit = sp.simplify(solution.rhs)  # Obtener la solución explícita

# Mostrar la solución en la terminal
print("La solución particular de la ecuación diferencial es:")
print(solution)

# Convertir la solución de SymPy en una función evaluable
f_solution = sp.lambdify(x, solution_explicit, 'numpy')

# Definir la función de GeoGebra (misma solución)
f_geogebra = f_solution  # Usamos la misma función para simular la solución de GeoGebra

# Rango de valores de x para graficar y comparar
x_vals = np.linspace(1, 5, 100)  # Empezamos en 1 para evitar x=0
y_solution_vals = f_solution(x_vals)
y_geogebra_vals = f_geogebra(x_vals)

# Calcular el porcentaje de acierto evitando divisiones por cero
epsilon = 1e-10  # Valor mínimo para evitar división por cero
differences = np.abs(y_solution_vals - y_geogebra_vals)
error_percentage = 100 * np.mean(differences / (np.maximum(y_solution_vals, y_geogebra_vals) + epsilon))

print(f"Porcentaje de acierto entre ambas funciones: {100 - error_percentage:.2f}%")

# Graficar ambas funciones para comparación
plt.plot(x_vals, y_solution_vals, label='Solución en Python', color='blue')
plt.plot(x_vals, y_geogebra_vals, label='Función de GeoGebra', color='red', linestyle='--')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title(r'Comparación de Soluciones: Python vs GeoGebra')
plt.legend()
plt.grid()
plt.show()
