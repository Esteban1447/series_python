import pandas as pd

n = int(input("¿Cuántos libros deseas registrar? "))

libros = {}
for i in range(n):
    titulo = input(f"Ingrese el título del libro #{i+1}: ")
    prestamos = int(input(f"Ingrese el número de préstamos de '{titulo}': "))
    libros[titulo] = prestamos

serie_prestamos = pd.Series(libros)

print("\nSerie de préstamos de libros:")
print(serie_prestamos)

libro_mas_prestado = serie_prestamos.idxmax()
libro_menos_prestado = serie_prestamos.idxmin()

print(f"\nLibro más prestado: {libro_mas_prestado} ({serie_prestamos.max()} préstamos)")
print(f"Libro menos prestado: {libro_menos_prestado} ({serie_prestamos.min()} préstamos)")

total_prestamos = serie_prestamos.sum()
print(f"\nTotal de préstamos del mes: {total_prestamos}")

print("\nCirculación por libro:")
for libro, cantidad in serie_prestamos.items():
    if cantidad > 15:
        print(f"{libro}: Alta circulación ({cantidad} préstamos)")
    else:
        print(f"{libro}: Baja circulación ({cantidad} préstamos)")
