# Dashboard Personal - Programación Orientada a Objetos

## Información del Estudiante
- **Nombre:** Edwin Ismar Armijso Flores
- **Carrera:** Ingeniería en Tecnologías de la Información y Comunicación
- **Universidad:** Universidad Estatal Amazónica (UEA)
- **Materia:** Programación Orientada a Objetos

## Descripción del Proyecto

Este proyecto es una adaptación personalizada del Dashboard de POO, diseñado para organizar y gestionar tareas, proyectos y actividades relacionadas con la asignatura de Programación Orientada a Objetos.

## Características Principales

### 🎯 Gestión de Proyectos
- Creación y organización de proyectos
- Seguimiento del progreso por proyecto
- Agrupación lógica de tareas relacionadas

### 📝 Sistema de Tareas
- Tareas individuales y por proyecto
- Estados: Pendiente, En Progreso, Completada
- Prioridades: Alta, Media, Baja
- Fechas de vencimiento
- Sistema de comentarios

### 📊 Estadísticas y Reportes
- Resumen general del progreso
- Estadísticas por estado de tareas
- Porcentaje de completitud
- Contadores de proyectos y tareas

### 💾 Persistencia de Datos
- Almacenamiento automático en JSON
- Carga automática al iniciar
- Historial de comentarios y cambios

## Instalación y Uso

### Requisitos
- Python 3.7 o superior
- Librerías estándar de Python (no requiere instalaciones adicionales)

### Instalación
```bash
# Clonar el repositorio
git clone https://github.com/Isyeday03/POO-Dashboard-Edwin-Armijos.git

# Navegar al directorio
cd POO-Dashboard-Edwin-Armijos

# Ejecutar el dashboard
python Dashboard.py
```

### Uso Básico

1. **Ejecutar el programa:**
   ```bash
   python Dashboard.py
   ```

2. **Navegación del menú:**
   - Opción 1: Crear nuevo proyecto
   - Opción 2: Crear nueva tarea
   - Opción 3: Listar proyectos
   - Opción 4: Listar tareas individuales
   - Opción 5: Cambiar estado de tarea
   - Opción 6: Agregar comentario a tarea
   - Opción 7: Mostrar estadísticas
   - Opción 8: Salir

## Estructura del Proyecto

```
POO-Dashboard-[TuNombre]/
├── Dashboard.py          # Archivo principal del dashboard
├── README.md            # Este archivo
├── dashboard_data.json  # Archivo de datos (se crea automáticamente)
├── ejemplos/            # Carpeta con ejemplos de uso
└── docs/               # Documentación adicional
```

## Clases Principales

### Clase `Tarea`
Representa una tarea individual con:
- ID único
- Título y descripción
- Fechas de creación y vencimiento
- Estado y prioridad
- Sistema de comentarios

### Clase `Proyecto`
Representa un proyecto que contiene múltiples tareas:
- ID único
- Nombre y descripción
- Lista de tareas asociadas
- Cálculo automático de progreso

### Clase `Dashboard`
Clase principal que gestiona:
- Proyectos y tareas
- Persistencia de datos
- Estadísticas y reportes
- Interfaz de usuario

## Personalización Realizada

### Adaptaciones Principales:
1. **Interfaz de usuario mejorada** con menús claros y navegación intuitiva
2. **Sistema de persistencia** para mantener datos entre sesiones
3. **Estadísticas detalladas** para seguimiento del progreso
4. **Comentarios y seguimiento** para documentar el proceso de aprendizaje
5. **Organización por proyectos** para agrupar tareas relacionadas

### Mejoras Específicas para POO:
- Estructura orientada a objetos bien definida
- Encapsulación de datos y funcionalidades
- Métodos específicos para cada responsabilidad
- Reutilización de código mediante clases

## Ejemplos de Uso

### Crear un Proyecto
```python
dashboard = Dashboard()
proyecto = dashboard.crear_proyecto("Conceptos Básicos POO", "Ejercicios sobre clases y objetos")
```

### Crear una Tarea
```python
tarea = dashboard.crear_tarea(
    "Implementar clase Estudiante",
    "Crear clase con atributos nombre, edad, carrera",
    fecha_vencimiento="2024-12-15",
    prioridad="alta",
    proyecto_id=1
)
```

### Cambiar Estado de Tarea
```python
tarea = dashboard.obtener_tarea(1)
tarea.cambiar_estado("completada")
```

## Contribución

Este proyecto fue desarrollado como parte de la asignatura de Programación Orientada a Objetos. Las contribuciones y mejoras son bienvenidas.

## Licencia

Este proyecto es parte del material educativo de la Universidad Estatal Amazónica y está destinado únicamente para fines académicos.

## Contacto

- **Estudiante:** Edwin Ismar Armijos Flores
- **Email:** [eiarmijosf@uea.edu.ec]
- **Repositorio:** https://github.com/Isyeday03/POO-Dashboard-Edwin-Armijos

---

*Desarrollado con ❤️ para el aprendizaje de Programación Orientada a Objetos*