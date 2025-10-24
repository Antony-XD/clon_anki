# Lista de tarjetas (flashcards)
# Cada elemento es una pareja: (pregunta, respuesta)
flashcards = [
    ("Capital de Francia", "París"),
    ("2 + 2", "4"),
    ("Color del cielo", "Azul"),
    ("quien descubrio la curva del olvido", "Hermann Ebbinghaus en 1885"),
]

# Muestra el título del programa en pantalla
print("=== Flash Cards 🧠 ===\n")

# Recorre una por una las tarjetas de la lista
# "pregunta" toma el primer valor de la pareja y "respuesta" el segundo
for pregunta, respuesta in flashcards:
    # Muestra la pregunta
    print(f"Pregunta: {pregunta}")
    
    # Espera a que el usuario presione ENTER antes de mostrar la respuesta
    input("Presiona ENTER para ver la respuesta...")
    
    # Muestra la respuesta correspondiente
    print(f"Respuesta: {respuesta}\n")
    
    # Espera otra vez antes de pasar a la siguiente tarjeta
    input("Presiona ENTER para continuar...\n")

# Cuando se acaban todas las tarjetas, muestra un mensaje final
print("¡Has terminado todas las tarjetas!")
