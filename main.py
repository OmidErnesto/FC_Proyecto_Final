import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Datos
M = 7.35e22  # Masa de la Luna en kg
MT = 5.98e24  # Masa de la Tierra en kg
R = 6.37e6  # Radio de la Tierra en metros
r = 3.84e8  # Distancia Tierra-Luna en metros
theta_values = np.linspace(0, 2 * np.pi, 1000)  # Valores de theta en radianes

# Cálculo de la elevación de la capa de agua
def calculate_elevation(theta):
    return (M / (2 * MT)) * (R / r) ** 3 * R * (3 * np.cos(theta) ** 2 - 1)

# Crear la figura y los ejes
fig, (ax_main, ax_elevation) = plt.subplots(nrows=2, figsize=(10, 10))
ax_main.set_xlim(-1.5 * r, 1.5 * r)
ax_main.set_ylim(-1.5 * r, 1.5 * r)
ax_main.set_aspect('equal')

# Círculo de la Tierra
earth_circle = plt.Circle((0, 0), R, color='blue', alpha=0.5)
ax_main.add_artist(earth_circle)

# Inicializar la posición de la Luna
moon, = ax_main.plot([], [], 'ro')

# Inicializar la elevación
elevation_line, = ax_main.plot([], [], label='Distancia Tierra-Luna', color='green')

# Función de inicialización de la animación
def init():
    moon.set_data([], [])
    elevation_line.set_data([], [])
    return moon, elevation_line

# Función de actualización de la animación
def update(frame):
    theta = frame * (2 * np.pi / 180)  # Convertir a radianes
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    moon.set_data(x, y)
    
    elevation = calculate_elevation(theta)
    elevation_line.set_data([x, 0], [y, elevation])
    
    # Agregar variación de la elevación en la subgráfica
    ax_elevation.plot(frame, elevation * 10, 'go')
    
    return moon, elevation_line

# Crear la animación
animation = FuncAnimation(fig, update, frames=360, init_func=init, blit=True)

# Etiquetas y título del gráfico principal
ax_main.set_xlabel('Distancia X (metros)')
ax_main.set_ylabel('Distancia Y (metros)')
ax_main.set_title('Órbita de la Luna alrededor de la Tierra y Elevación de la Capa de Agua')
ax_main.legend()
ax_main.grid()

# Etiquetas y título de la subgráfica de elevación
ax_elevation.set_xlabel('Frames')
ax_elevation.set_ylabel('Elevación de la Capa de Agua')
ax_elevation.set_title('Variación de la Elevación de la Capa de Agua')
ax_elevation.grid()

# Ajustar el espacio entre las subgráficas
plt.tight_layout()

# Mostrar la animación
plt.show()
