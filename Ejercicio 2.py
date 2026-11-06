curso_A = {"Ana", "Carlos", "Laura", "Pedro", "Sofia", "Andres", "Camila"}
curso_B = {"Laura", "Pedro", "Daniel", "Sofia", "Mateo", "Valentina"}

print(" 1. Estudiantes inscritos en cada curso:")
print(f"Curso A (Fundamentos de programación): {curso_A}")
print(f"Curso B (Introducción a bases de datos): {curso_B}\n")


todos_estudiantes = curso_A | curso_B
print(" 2. Estudiantes diferentes inscritos entre los dos cursos:")
print(f"Total de estudiantes únicos: {len(todos_estudiantes)}")
print(f"Listado: {todos_estudiantes}\n")


ambos_cursos = curso_A & curso_B
print("3. Estudiantes inscritos en ambos cursos ")
print(f"Estudiantes: {ambos_cursos}\n")


unicos_A = curso_A - curso_B
print("4. Estudiantes inscritos únicamente en el curso A ")
print(f"Estudiantes: {unicos_A}\n")


unicos_B = curso_B - curso_A
print("5. Estudiantes inscritos únicamente en el curso B ")
print(f"Estudiantes: {unicos_B}\n")

exactamente_uno = curso_A ^ curso_B
print("6. Estudiantes inscritos en exactamente uno de los dos cursos ")
print(f"Estudiantes: {exactamente_uno}\n")

a_en_b = curso_A.issubset(curso_B)
print("7. ¿Todos los estudiantes del curso A están en el curso B? ")
print(f"Respuesta: {a_en_b} (No todos los de A están en B)\n")


print("8. Agregar un nuevo estudiante y actualizar resultados ")
nuevo_curso = input("A qué curso desea agregar al estudiante (A o B)?: ")
nuevo_nombre = input("Ingrese el nombre del nuevo estudiante: ")

if nuevo_curso == 'A':
    curso_A.add(nuevo_nombre)
    print(f"\n¡{nuevo_nombre} ha sido agregado exitosamente al Curso A!")
elif nuevo_curso == 'B':
    curso_B.add(nuevo_nombre)
    print(f"\n¡{nuevo_nombre} ha sido agregado exitosamente al Curso B!")
else:
    print("\n Error, digite solamente un caracter A o B.")


print("\n---Modificaciones realizadas---")
print(f"Curso A actual: {curso_A}")
print(f"Curso B actual: {curso_B}")
print(f"Nuevo total de estudiantes diferentes: {len(curso_A | curso_B)}")
print(f"Nuevos estudiantes en ambos cursos: {curso_A & curso_B}")
