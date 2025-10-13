flashcards = [
    ("Capital de Francia", "París"),
    ("2 + 2", "4"),
    ("Color del cielo", "Azul"),
    ("quien decubrio la curva del olvido", "Hermann Ebbinghaus en 1885"),
]

print("=== Flash Cards 🧠 ===\n")

for pregunta, respuesta in flashcards:
    print(f"Pregunta: {pregunta}")
    input("Presiona ENTER para ver la respuesta...")
    print(f"Respuesta: {respuesta}\n")
    input("Presiona ENTER para continuar...\n")

print("¡Has terminado todas las tarjetas!")