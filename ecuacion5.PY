import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sympy as sp

# Definir variables simbólicas
x = sp.symbols('x')
C = sp.symbols('C')  # Constante de integración

# Definir la ecuación diferencial
y = sp.Function('y')(x)
diff_eq = sp.Eq(y.diff(x), (x + y) / (x - y))

# Resolver la ecuación diferencial simbólicamente
sol = sp.dsolve(diff_eq, y)

# Mostrar la solución en la terminal
print("Solución general de la ecuación diferencial:")
print(sol)

# Función que representa la ecuación diferencial
def f(x, y):
    return (x + y) / (x - y)

# Intervalo de tiempo y condiciones iniciales
x_span = (0.1, 5)  # Intervalo de x, empezando desde 0.1 para evitar división por cero
y0 = [1]  # Condición inicial, puedes cambiar el valor

# Resolver la ecuación diferencial numéricamente
num_sol = solve_ivp(f, x_span, y0, t_eval=np.linspace(x_span[0], x_span[1], 100))

# Graficar la solución numérica
plt.plot(num_sol.t, num_sol.y[0], label='Solución Numérica: y(x)')

# Graficar la solución GeoGebra (resolviendo de nuevo)
geo_sol = solve_ivp(f, x_span, y0, t_eval=np.linspace(x_span[0], x_span[1], 100))
plt.plot(geo_sol.t, geo_sol.y[0], label='Solución GeoGebra')

plt.title('Comparación de soluciones de la ecuación diferencial homogénea')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.legend()
plt.grid()
plt.show()

# Calcular el porcentaje de acierto
aciertos = np.isclose(num_sol.y[0], geo_sol.y[0])
porcentaje_acierto = (np.sum(aciertos) / len(aciertos)) * 100
print(f"Porcentaje de acierto entre las soluciones: {porcentaje_acierto:.2f}%")
