"""
Dashboard para Programación Orientada a Objetos
Universidad Estatal Amazónica
Carrera: Ingeniería en Tecnologías de la Información y Comunicación

Autor: Edwin Ismar Armijos Flores
Descripción: Sistema de gestión de tareas y proyectos para la materia de POO
"""

import datetime
import json
import os
from typing import List, Dict, Optional


class Tarea:
    """Clase para representar una tarea individual"""

    def __init__(self, id: int, titulo: str, descripcion: str,
                 fecha_creacion: str = None, fecha_vencimiento: str = None,
                 estado: str = "pendiente", prioridad: str = "media"):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado  # pendiente, en_progreso, completada
        self.prioridad = prioridad  # urgente, normal, leve
        self.comentarios = []

    def agregar_comentario(self, comentario: str):
        """Agrega un comentario a la tarea"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.comentarios.append(f"[{timestamp}] {comentario}")

    def cambiar_estado(self, nuevo_estado: str):
        """Cambia el estado de la tarea"""
        estados_validos = ["pendiente", "en_progreso", "completada"]
        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
            self.agregar_comentario(f"Estado cambiado a: {nuevo_estado}")
        else:
            raise ValueError(f"Estado no válido. Usar: {estados_validos}")

    def __str__(self):
        return f"[{self.id}] {self.titulo} - {self.estado.upper()}"


class Proyecto:
    """Clase para representar un proyecto que contiene múltiples tareas"""

    def __init__(self, id: int, nombre: str, descripcion: str):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.tareas = []
        self.fecha_creacion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def agregar_tarea(self, tarea: Tarea):
        """Agrega una tarea al proyecto"""
        self.tareas.append(tarea)

    def obtener_progreso(self) -> Dict:
        """Calcula el progreso del proyecto"""
        if not self.tareas:
            return {"total": 0, "completadas": 0, "porcentaje": 0}

        total = len(self.tareas)
        completadas = sum(1 for tarea in self.tareas if tarea.estado == "completada")
        porcentaje = (completadas / total) * 100

        return {
            "total": total,
            "completadas": completadas,
            "porcentaje": round(porcentaje, 2)
        }

    def __str__(self):
        progreso = self.obtener_progreso()
        return f"Proyecto: {self.nombre} - {progreso['porcentaje']}% completado"


class Dashboard:
    """Clase principal del dashboard para gestionar tareas y proyectos de POO"""

    def __init__(self):
        self.proyectos = []
        self.tareas_individuales = []
        self.siguiente_id_proyecto = 1
        self.siguiente_id_tarea = 1
        self.archivo_datos = "dashboard_data.json"
        self.cargar_datos()

    def crear_proyecto(self, nombre: str, descripcion: str) -> Proyecto:
        """Crea un nuevo proyecto"""
        proyecto = Proyecto(self.siguiente_id_proyecto, nombre, descripcion)
        self.proyectos.append(proyecto)
        self.siguiente_id_proyecto += 1
        self.guardar_datos()
        return proyecto

    def crear_tarea(self, titulo: str, descripcion: str,
                    fecha_vencimiento: str = None, prioridad: str = "media",
                    proyecto_id: int = None) -> Tarea:
        """Crea una nueva tarea"""
        tarea = Tarea(self.siguiente_id_tarea, titulo, descripcion,
                      fecha_vencimiento=fecha_vencimiento, prioridad=prioridad)

        if proyecto_id:
            proyecto = self.obtener_proyecto(proyecto_id)
            if proyecto:
                proyecto.agregar_tarea(tarea)
            else:
                raise ValueError(f"Proyecto con ID {proyecto_id} no encontrado")
        else:
            self.tareas_individuales.append(tarea)

        self.siguiente_id_tarea += 1
        self.guardar_datos()
        return tarea

    def obtener_proyecto(self, id: int) -> Optional[Proyecto]:
        """Obtiene un proyecto por ID"""
        for proyecto in self.proyectos:
            if proyecto.id == id:
                return proyecto
        return None

    def obtener_tarea(self, id: int) -> Optional[Tarea]:
        """Obtiene una tarea por ID (busca en proyectos y tareas individuales)"""
        # Buscar en tareas individuales
        for tarea in self.tareas_individuales:
            if tarea.id == id:
                return tarea

        # Buscar en proyectos
        for proyecto in self.proyectos:
            for tarea in proyecto.tareas:
                if tarea.id == id:
                    return tarea

        return None

    def listar_proyectos(self):
        """Lista todos los proyectos"""
        if not self.proyectos:
            print("No hay proyectos creados.")
            return

        print("\n=== PROYECTOS ===")
        for proyecto in self.proyectos:
            print(f"{proyecto}")
            if proyecto.tareas:
                for tarea in proyecto.tareas:
                    print(f"  - {tarea}")

    def listar_tareas_individuales(self):
        """Lista todas las tareas individuales"""
        if not self.tareas_individuales:
            print("No hay tareas individuales.")
            return

        print("\n=== TAREAS INDIVIDUALES ===")
        for tarea in self.tareas_individuales:
            print(f"{tarea}")

    def obtener_estadisticas(self) -> Dict:
        """Obtiene estadísticas generales del dashboard"""
        total_proyectos = len(self.proyectos)
        total_tareas = len(self.tareas_individuales)

        # Contar tareas en proyectos
        for proyecto in self.proyectos:
            total_tareas += len(proyecto.tareas)

        # Contar tareas por estado
        tareas_pendientes = 0
        tareas_en_progreso = 0
        tareas_completadas = 0

        for tarea in self.tareas_individuales:
            if tarea.estado == "pendiente":
                tareas_pendientes += 1
            elif tarea.estado == "en_progreso":
                tareas_en_progreso += 1
            elif tarea.estado == "completada":
                tareas_completadas += 1

        for proyecto in self.proyectos:
            for tarea in proyecto.tareas:
                if tarea.estado == "pendiente":
                    tareas_pendientes += 1
                elif tarea.estado == "en_progreso":
                    tareas_en_progreso += 1
                elif tarea.estado == "completada":
                    tareas_completadas += 1

        return {
            "total_proyectos": total_proyectos,
            "total_tareas": total_tareas,
            "tareas_pendientes": tareas_pendientes,
            "tareas_en_progreso": tareas_en_progreso,
            "tareas_completadas": tareas_completadas,
            "porcentaje_completado": round((tareas_completadas / total_tareas * 100), 2) if total_tareas > 0 else 0
        }

    def mostrar_estadisticas(self):
        """Muestra las estadísticas del dashboard"""
        stats = self.obtener_estadisticas()

        print("\n" + "=" * 50)
        print("ESTADÍSTICAS DEL DASHBOARD - POO")
        print("=" * 50)
        print(f"Total de proyectos: {stats['total_proyectos']}")
        print(f"Total de tareas: {stats['total_tareas']}")
        print(f"Tareas pendientes: {stats['tareas_pendientes']}")
        print(f"Tareas en progreso: {stats['tareas_en_progreso']}")
        print(f"Tareas completadas: {stats['tareas_completadas']}")
        print(f"Porcentaje completado: {stats['porcentaje_completado']}%")
        print("=" * 50)

    def guardar_datos(self):
        """Guarda los datos en un archivo JSON"""
        try:
            datos = {
                "proyectos": [],
                "tareas_individuales": [],
                "siguiente_id_proyecto": self.siguiente_id_proyecto,
                "siguiente_id_tarea": self.siguiente_id_tarea
            }

            # Serializar proyectos
            for proyecto in self.proyectos:
                proyecto_data = {
                    "id": proyecto.id,
                    "nombre": proyecto.nombre,
                    "descripcion": proyecto.descripcion,
                    "fecha_creacion": proyecto.fecha_creacion,
                    "tareas": []
                }

                for tarea in proyecto.tareas:
                    tarea_data = {
                        "id": tarea.id,
                        "titulo": tarea.titulo,
                        "descripcion": tarea.descripcion,
                        "fecha_creacion": tarea.fecha_creacion,
                        "fecha_vencimiento": tarea.fecha_vencimiento,
                        "estado": tarea.estado,
                        "prioridad": tarea.prioridad,
                        "comentarios": tarea.comentarios
                    }
                    proyecto_data["tareas"].append(tarea_data)

                datos["proyectos"].append(proyecto_data)

            # Serializar tareas individuales
            for tarea in self.tareas_individuales:
                tarea_data = {
                    "id": tarea.id,
                    "titulo": tarea.titulo,
                    "descripcion": tarea.descripcion,
                    "fecha_creacion": tarea.fecha_creacion,
                    "fecha_vencimiento": tarea.fecha_vencimiento,
                    "estado": tarea.estado,
                    "prioridad": tarea.prioridad,
                    "comentarios": tarea.comentarios
                }
                datos["tareas_individuales"].append(tarea_data)

            with open(self.archivo_datos, 'w', encoding='utf-8') as f:
                json.dump(datos, f, ensure_ascii=False, indent=2)

        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def cargar_datos(self):
        """Carga los datos desde un archivo JSON"""
        try:
            if os.path.exists(self.archivo_datos):
                with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                    datos = json.load(f)

                self.siguiente_id_proyecto = datos.get("siguiente_id_proyecto", 1)
                self.siguiente_id_tarea = datos.get("siguiente_id_tarea", 1)

                # Cargar proyectos
                for proyecto_data in datos.get("proyectos", []):
                    proyecto = Proyecto(
                        proyecto_data["id"],
                        proyecto_data["nombre"],
                        proyecto_data["descripcion"]
                    )
                    proyecto.fecha_creacion = proyecto_data["fecha_creacion"]

                    # Cargar tareas del proyecto
                    for tarea_data in proyecto_data.get("tareas", []):
                        tarea = Tarea(
                            tarea_data["id"],
                            tarea_data["titulo"],
                            tarea_data["descripcion"],
                            tarea_data["fecha_creacion"],
                            tarea_data.get("fecha_vencimiento"),
                            tarea_data["estado"],
                            tarea_data["prioridad"]
                        )
                        tarea.comentarios = tarea_data.get("comentarios", [])
                        proyecto.agregar_tarea(tarea)

                    self.proyectos.append(proyecto)

                # Cargar tareas individuales
                for tarea_data in datos.get("tareas_individuales", []):
                    tarea = Tarea(
                        tarea_data["id"],
                        tarea_data["titulo"],
                        tarea_data["descripcion"],
                        tarea_data["fecha_creacion"],
                        tarea_data.get("fecha_vencimiento"),
                        tarea_data["estado"],
                        tarea_data["prioridad"]
                    )
                    tarea.comentarios = tarea_data.get("comentarios", [])
                    self.tareas_individuales.append(tarea)

        except Exception as e:
            print(f"Error al cargar datos: {e}")


def menu_principal():
    """Función principal del menú interactivo"""
    dashboard = Dashboard()

    while True:
        print("\n" + "=" * 50)
        print("DASHBOARD - PROGRAMACIÓN ORIENTADA A OBJETOS")
        print("=" * 50)
        print("1. Crear nuevo proyecto")
        print("2. Crear nueva tarea")
        print("3. Listar proyectos")
        print("4. Listar tareas individuales")
        print("5. Cambiar estado de tarea")
        print("6. Agregar comentario a tarea")
        print("7. Mostrar estadísticas")
        print("8. Salir")

        try:
            opcion = input("\nSelecciona una opción (1-8): ").strip()

            if opcion == "1":
                nombre = input("Nombre del proyecto: ").strip()
                descripcion = input("Descripción: ").strip()
                proyecto = dashboard.crear_proyecto(nombre, descripcion)
                print(f"✓ Proyecto '{proyecto.nombre}' creado exitosamente!")

            elif opcion == "2":
                titulo = input("Título de la tarea: ").strip()
                descripcion = input("Descripción: ").strip()
                fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD, opcional): ").strip()
                prioridad = input("Prioridad (alta/media/baja): ").strip() or "media"

                # Preguntar si es para un proyecto
                if dashboard.proyectos:
                    print("\nProyectos disponibles:")
                    for proyecto in dashboard.proyectos:
                        print(f"  {proyecto.id}. {proyecto.nombre}")

                    proyecto_id = input("ID del proyecto (dejar vacío para tarea individual): ").strip()
                    proyecto_id = int(proyecto_id) if proyecto_id else None
                else:
                    proyecto_id = None

                tarea = dashboard.crear_tarea(
                    titulo, descripcion,
                    fecha_vencimiento or None,
                    prioridad,
                    proyecto_id
                )
                print(f"✓ Tarea '{tarea.titulo}' creada exitosamente!")

            elif opcion == "3":
                dashboard.listar_proyectos()

            elif opcion == "4":
                dashboard.listar_tareas_individuales()

            elif opcion == "5":
                tarea_id = int(input("ID de la tarea: "))
                tarea = dashboard.obtener_tarea(tarea_id)
                if tarea:
                    print(f"Tarea actual: {tarea}")
                    nuevo_estado = input("Nuevo estado (pendiente/en_progreso/completada): ").strip()
                    tarea.cambiar_estado(nuevo_estado)
                    dashboard.guardar_datos()
                    print(f"✓ Estado actualizado a '{nuevo_estado}'")
                else:
                    print("Tarea no encontrada.")

            elif opcion == "6":
                tarea_id = int(input("ID de la tarea: "))
                tarea = dashboard.obtener_tarea(tarea_id)
                if tarea:
                    comentario = input("Comentario: ").strip()
                    tarea.agregar_comentario(comentario)
                    dashboard.guardar_datos()
                    print("✓ Comentario agregado.")
                else:
                    print("Tarea no encontrada.")

            elif opcion == "7":
                dashboard.mostrar_estadisticas()

            elif opcion == "8":
                print("¡Gracias por usar el Dashboard de POO!")
                break

            else:
                print("Opción no válida. Intenta de nuevo.")

        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n¡Hasta luego!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    # Ejemplo de uso y pruebas
    print("Dashboard de Programación Orientada a Objetos")
    print("Universidad Estatal Amazónica")
    print("Carrera: Ingeniería en Tecnologías de la Información y Comunicación")
    print("\nIniciando sistema...")

    menu_principal()

