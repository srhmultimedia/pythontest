import streamlit as st
import random

# Datos de los boxeadores
boxeador_1 = {
    "nombre": "Carlos 'El Toro' Rodríguez",
    "ganadas": 5,
    "perdidas": 5,
    "imagen": "https://marketplace.canva.com/jwW4U/MAEJX3jwW4U/1/s2/canva-male-muay-thai-boxer--MAEJX3jwW4U.jpg"  # Aquí deberías colocar la URL de la imagen del boxeador 1
}

boxeador_2 = {
    "nombre": "Juan 'El Jaguar' Pérez",
    "ganadas": 5,
    "perdidas": 5,
    "imagen": "https://marketplace.canva.com/K79wM/MAEtM1K79wM/1/s2/canva-a-man-doing-boxing-MAEtM1K79wM.jpg"  # Aquí deberías colocar la URL de la imagen del boxeador 2
}

# Calcular probabilidades
def calcular_probabilidades(boxeador):
    total_peleas = boxeador["ganadas"] + boxeador["perdidas"]
    prob_victoria = boxeador["ganadas"] / total_peleas
    prob_derrota = boxeador["perdidas"] / total_peleas
    return prob_victoria, prob_derrota

prob_victoria_1, prob_derrota_1 = calcular_probabilidades(boxeador_1)
prob_victoria_2, prob_derrota_2 = calcular_probabilidades(boxeador_2)

# Simulación de pelea
def simular_pelea(prob_victoria_1, prob_victoria_2):
    resultado = random.choices(
        population=[boxeador_1["nombre"], boxeador_2["nombre"]],
        weights=[prob_victoria_1, prob_victoria_2],
        k=1
    )
    return resultado[0]

ganador = simular_pelea(prob_victoria_1, prob_victoria_2)

# Frontend con Streamlit
st.title("Simulación de Pelea de Box")

# Mostrar imágenes y ganador
st.image(boxeador_1["imagen"], caption=boxeador_1["nombre"], use_column_width=True)
st.image(boxeador_2["imagen"], caption=boxeador_2["nombre"], use_column_width=True)

st.header("Resultado")
st.write(f"¡El ganador es: **{ganador}**!")
