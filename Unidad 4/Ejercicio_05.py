print("➖➖➖➖➖➖ Eliminar o Agregar ➖➖➖➖➖➖➖➖")

Student_Attendance = ["Ana", "Luis", "Carlos", "Mario", "Maria", "Sebastian", "Joaquin", "Franco"]

print(f"\nLista Original: {sorted(Student_Attendance)} ")
while True:
    User_Option = str(input("\n➡️  Quiere Ingresar un Alumno o Eliminar Uno ? (1 : Agregar , 2 : Eliminar , 0 : Salir): "))
    if User_Option == "0":
        break
    elif User_Option == "1":
        name = str(input("\n➡️  Ingrese el Nombre del Alumno  ➕  : "))
        Student_Attendance.append(name)
        print(f"\n✅  Lista Actualizada: {sorted(Student_Attendance)} ")
    elif User_Option == "2":
        name = str(input("\n➡️  Ingrese el Nombre del Alumno a Eliminar  ❌ : "))
        if name in Student_Attendance:
            Student_Attendance.remove(name)
            print(f"\n✅  Lista Actualizada: {sorted(Student_Attendance)} ")
        else:
            print(f"El alumno {name} no está en la lista.")
print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")