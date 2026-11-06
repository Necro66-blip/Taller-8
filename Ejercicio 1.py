v = [
    [12, 15, 10, 18],
    [8, 14, 16, 12],
    [20, 18, 15, 22]
]

print("Ventas")
print("V1:", v[0])
print("V2:", v[1])
print("V3:", v[2])

tv = [sum(f) for f in v]
ts = [sum(v[i][j] for i in range(len(v))) for j in range(len(v[0]))]

for i, s in enumerate(tv):
    print(f"Total Vendedor {i+1}: {s}")

for j, s in enumerate(ts):
    print(f"Total Semana {j+1}: {s}")

print(f"Mejor vendedor: Vendedor {tv.index(max(tv))+1}")
print(f"Mejor semana: Semana {ts.index(max(ts))+1}")

ntot = sum(tv)
cant = len(v) * len(v[0])
print(f"Promedio general: {ntot / cant:}")

fv = int(input("Ingrese vendedor (1-3): ")) - 1
cs = int(input("Ingrese semana (1-4): ")) - 1
nv = int(input("Ingrese nuevo valor: "))
v[fv][cs] = nv

print("Matriz actualizada:")
for f in v:
    print(f)
