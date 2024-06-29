import random

# Datos de los boxeadores
boxeador_1 = {
    "nombre": "Carlos 'El Toro' Rodríguez",
    "ganadas": 5,
    "perdidas": 5,
}

boxeador_2 = {
    "nombre": "Juan 'El Jaguar' Pérez",
    "ganadas": 5,
    "perdidas": 5,
}

# Calcular probabilidades
def calcular_probabilidades(boxeador):
    total_peleas = boxeador["ganadas"] + boxeador["perdidas"]
    prob_victoria = boxeador["ganadas"] / total_peleas
    prob_derrota = boxeador["perdidas"] / total_peleas
    return prob_victoria, prob_derrota

prob_victoria_1, prob_derrota_1 = calcular_probabilidades(boxeador_1)
prob_victoria_2, prob_derrota_2 = calcular_probabilidades(boxeador_2)

#print(f"Probabilidades de {boxeador_1['nombre']}: Victoria = {prob_victoria_1:.2f}, Derrota = {prob_derrota_1:.2f}")
#print(f"Probabilidades de {boxeador_2['nombre']}: Victoria = {prob_victoria_2:.2f}, Derrota = {prob_derrota_2:.2f}")

# Simulación de pelea
def simular_pelea(prob_victoria_1, prob_victoria_2):
    resultado = random.choices(
        population=[boxeador_1["nombre"], boxeador_2["nombre"]],
        weights=[prob_victoria_1, prob_victoria_2],
        k=1
    )
    return resultado[0]

ganador = simular_pelea(prob_victoria_1, prob_victoria_2)
print(f"El ganador de la pelea es: {ganador}")
