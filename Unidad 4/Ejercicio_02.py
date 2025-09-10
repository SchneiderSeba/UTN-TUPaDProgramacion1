print("➖➖➖➖➖➖ Ingresar Item y Borrarlos ➖➖➖➖➖➖➖➖")

Item_List = []

for i in range(5):
    item = str(input(f"\n➡️  Ingrese el Item {i + 1}: "))
    Item_List.append(item)

print(f"\n{sorted(Item_List)}")

user_choice = str(input("\n☠️  ¿Desea Eliminar un Item? (si/no): "))

if user_choice.lower() == "si":
    item_to_remove = str(input("\n➡️  Ingrese el Item a Eliminar: "))
    if item_to_remove in Item_List:
        Item_List.remove(item_to_remove)
        print(f"\nItem '{item_to_remove}' eliminado.")
    else:
        print(f"\nItem '{item_to_remove}' no encontrado en la lista.")
else:
    print("\nTerminamos .")

print(f"\n✅  Lista Actualizada: {sorted(Item_List)}")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")