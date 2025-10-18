def leer_temperaturas():
    """Lee las temperaturas desde el archivo 'temperaturas.txt' y retorna una lista de valores float."""
    nombre_archivo = "temperaturas.txt"
    temperaturas = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                try:
                    fecha, temp = linea.strip().split(',')
                    temperaturas.append(float(temp))
                except ValueError:
                    print(f"Línea inválida ignorada: {linea.strip()}")
        if not temperaturas:
            raise ValueError("El archivo no contiene datos válidos.")
        return temperaturas
    except FileNotFoundError:
        print(f"❌ El archivo '{nombre_archivo}' no existe.")
        return []
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return []


def escribir_resumen(promedio, maximo, minimo):
    """Escribe los resultados en un nuevo archivo 'resumen_temperaturas.txt'."""
    nombre_salida = "resumen_temperaturas.txt"
    try:
        with open(nombre_salida, 'w', encoding='utf-8') as f:
            f.write("Resumen de Temperaturas\n")
            f.write(f"Temperatura promedio: {promedio:.2f}°C\n")
            f.write(f"Temperatura máxima: {maximo:.2f}°C\n")
            f.write(f"Temperatura mínima: {minimo:.2f}°C\n")
        print(f"✅ Resultados guardados en '{nombre_salida}'")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")


def main():
    print("📊 Analizando temperaturas desde 'temperaturas.txt'...\n")
    temperaturas = leer_temperaturas()

    if temperaturas:
        promedio = sum(temperaturas) / len(temperaturas)
        maximo = max(temperaturas)
        minimo = min(temperaturas)

        print(f"Temperatura promedio: {promedio:.2f}°C")
        print(f"Temperatura máxima: {maximo:.2f}°C")
        print(f"Temperatura mínima: {minimo:.2f}°C\n")

        escribir_resumen(promedio, maximo, minimo)
    else:
        print("No se pudieron obtener datos de temperatura.")


if __name__ == "__main__":
    main()
