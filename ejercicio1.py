import pandas as pd

ventas = pd.Series([1200, 1500, None, 1300, 1600, None],
                   index=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"])

print("📊 Serie original de ventas:")
print(ventas)

ventas_filled = ventas.fillna(ventas.mean())
print("\n📌 Serie luego del tratamiento de los datos faltantes (rellenadas con el promedio):")
print(ventas_filled)

ventas_ordenadas = ventas_filled.sort_values()
print("\n📈 Ventas ordenadas de menor a mayor:")
print(ventas_ordenadas)

promedio = ventas_filled.mean()
minimo = ventas_filled.min()
maximo = ventas_filled.max()

print("\n📊 Estadísticas:")
print(f"Promedio: {promedio:.2f}")
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")

print("\n📅 Comparación mensual con el promedio:")
for mes in ventas_filled.index:
    if ventas_filled[mes] > promedio:
        print(f"{mes}: por encima del promedio")
    elif ventas_filled[mes] < promedio:
        print(f"{mes}: por debajo del promedio")
    else:
        print(f"{mes}: igual al promedio")
