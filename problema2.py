def crear_tabla(n):
    """Crea un archivo con la tabla de multiplicar del número n."""
    try:
        if n < 1 or n > 10:
            raise ValueError("El número debe estar entre 1 y 10.")
        nombre_archivo = f"tabla-{n}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            for i in range(1, 11):
                f.write(f"{n} x {i} = {n * i}\n")
        print(f"✅ Archivo '{nombre_archivo}' creado correctamente.")
    except Exception as e:
        print(f"❌ Error: {e}")


def leer_tabla(n):
    """Lee el archivo de la tabla de multiplicar del número n."""
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            print(f"\n📄 Contenido de '{nombre_archivo}':\n")
            print(f.read())
    except FileNotFoundError:
        print(f"❌ El archivo '{nombre_archivo}' no existe. Primero crea la tabla.")


def leer_linea_tabla(n, m):
    """Muestra una línea específica (m) de la tabla-n.txt."""
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()
            if m < 1 or m > len(lineas):
                print(f"⚠️ La línea {m} no existe en la tabla de {n}.")
            else:
                print(f"\n📌 Línea {m} del archivo '{nombre_archivo}':")
                print(lineas[m - 1].strip())
    except FileNotFoundError:
        print(f"❌ El archivo '{nombre_archivo}' no existe. Primero crea la tabla.")
    except Exception as e:
        print(f"Error: {e}")


def menu():
    while True:
        print("\n🧮 MENÚ DE TABLAS DE MULTIPLICAR")
        print("1. Crear tabla de multiplicar")
        print("2. Leer tabla completa")
        print("3. Leer una línea específica")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            try:
                n = int(input("Ingresa un número entre 1 y 10: "))
                crear_tabla(n)
            except ValueError:
                print("⚠️ Debes ingresar un número entero válido.")
        elif opcion == "2":
            try:
                n = int(input("Ingresa el número de la tabla que deseas leer: "))
                leer_tabla(n)
            except ValueError:
                print("⚠️ Debes ingresar un número entero válido.")
        elif opcion == "3":
            try:
                n = int(input("Ingresa el número de la tabla: "))
                m = int(input("Ingresa el número de línea que deseas ver (1–10): "))
                leer_linea_tabla(n, m)
            except ValueError:
                print("⚠️ Debes ingresar números enteros válidos.")
        elif opcion == "4":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida, intenta nuevamente.")


if __name__ == "__main__":
    menu()