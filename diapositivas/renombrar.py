import os
import re

def desplazar_desde_punto():
    # 1. Obtener archivos y filtrar por patrón n.html
    archivos = os.listdir('.')
    patron = re.compile(r'^(\d+)\.html$')
    
    lista_html = []
    for f in archivos:
        coincidencia = patron.match(f)
        if coincidencia:
            num = int(coincidencia.group(1))
            lista_html.append((num, f))
    
    if not lista_html:
        print("No se encontraron archivos con el formato n.html")
        return

    # 2. Preguntar al usuario el punto de inicio
    try:
        punto_inicio = int(input("¿Desde qué número quieres desplazar (ej: 6)? "))
    except ValueError:
        print("Entrada no válida. Debes ingresar un número entero.")
        return

    # 3. Filtrar solo los archivos iguales o mayores al punto de inicio
    # Y ordenarlos de mayor a menor para no sobrescribir
    a_desplazar = [x for x in lista_html if x[0] >= punto_inicio]
    a_desplazar.sort(key=lambda x: x[0], reverse=True)

    if not a_desplazar:
        print(f"No hay archivos iguales o mayores a {punto_inicio}.html para desplazar.")
        # Aun así, si el archivo no existe, podrías querer crearlo.
        if not os.path.exists(f"{punto_inicio}.html"):
            crear_vacio(punto_inicio)
        return

    print(f"Desplazando archivos desde el {punto_inicio} en adelante...")

    # 4. Renombrar (desplazar +1)
    for num, nombre_original in a_desplazar:
        nuevo_nombre = f"{num + 1}.html"
        try:
            os.rename(nombre_original, nuevo_nombre)
            print(f"Moviendo: {nombre_original} -> {nuevo_nombre}")
        except OSError as e:
            print(f"Error al mover {nombre_original}: {e}")

    # 5. Crear el nuevo archivo vacío en la posición elegida
    crear_vacio(punto_inicio)

def crear_vacio(numero):
    nombre = f"{numero}.html"
    with open(nombre, "w", encoding="utf-8") as f:
        f.write(f"")
    print(f"Hecho: '{nombre}' ha quedado libre y vacío.")

if __name__ == "__main__":
    desplazar_desde_punto()