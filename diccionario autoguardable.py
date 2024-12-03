import json

archivo = "JSON/lista.json"

try:
    with open(archivo, encoding='utf-8', mode="r") as f:
        dicc = json.load(f)
except FileNotFoundError:
    dicc = {}

def agregar_alumno():
    alumno = {}
    alumno["id"] = int(input("Número de alumno: "))
    alumno["datos"] = {}
    alumno["datos"]["nombre"] = input("Ingresa el nombre: ").strip()
    alumno["datos"]["apellidos"] = input("Ingresa los apellidos: ").strip()
    alumno["datos"]["fecha_nacimiento"] = input("Ingresa la fecha de nacimiento (DD/MM/AAAA): ").strip()
    alumno["datos"]["curso"] = input("Ingresa el nombre del curso: ").strip()
    alumno["notas"] = {}
    alumno["notas"]["ende"] = float(input("Ingresa la nota de ENDE: "))
    alumno["notas"]["programacion"] = float(input("Ingresa la nota de Programación: "))
    
    print("\nDatos del alumno:")
    print(f"  ID: {alumno['id']}")
    print("  Datos personales:")
    for detalle, dato in alumno["datos"].items():
        print(f"    {detalle.capitalize()}: {dato}")
    print("  Notas:")
    for asignatura, nota in alumno["notas"].items():
        print(f"    {asignatura.capitalize()}: {nota}")

    dicc[alumno["id"]] = alumno

    with open(archivo, "w", encoding='utf-8') as f:
        json.dump(dicc, f, ensure_ascii=False, indent=4)
    print("\nAlumno agregado correctamente y datos guardados en el archivo.")

if __name__ == "__main__":
    agregar_alumno()
