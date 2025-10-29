# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {("Lunes", "09:00"): "Reunión de equipo",
          ("Martes", "14:00"): "Almuerzo con cliente",
          ("Miércoles", "10:00"): "Presentación de proyecto"}

def consultar_evento(dia, hora):
    try:
        dia = str(dia)
        hora = str(hora)
    except ValueError:
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print("El día o la hora no son válidos, deben ser cadenas de texto ❌")
        return None

    evento = agenda.get((dia, hora))
    if evento:
        print(f"➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print(f"Evento encontrado: {evento} ✅")
    else:
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print("No hay eventos programados en ese día y hora ❌")

while True:

    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("📅 Agenda de Eventos - Consulta de Actividades:")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    dia = input("Ingrese el día de la semana: ").capitalize()
    hora = input("Ingrese la hora (HH:MM): ")
    consultar_evento(dia, hora)