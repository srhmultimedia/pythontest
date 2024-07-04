import streamlit as st
import random

# Puntajes de equipos
puntajes_equipos = {
    "Colombia": 0.01785,
    "Francia": 0.06608,
    "Etiopia": 0.06824,
    "Japón": 0.01785
}

# Calcular probabilidades
total_puntajes = sum(puntajes_equipos.values())
probabilidades = {equipo: puntaje / total_puntajes for equipo, puntaje in puntajes_equipos.items()}

# Simulación de la carrera
def simular_carrera(probabilidades):
    resultado = random.choices(
        population=list(probabilidades.keys()),
        weights=list(probabilidades.values()),
        k=1
    )
    return resultado[0]

# Frontend con Streamlit
st.title("Simulación de Carrera de Equipos")

# Mostrar probabilidades
st.subheader("Probabilidades de Ganar:")
for equipo, probabilidad in probabilidades.items():
    st.write(f"- {equipo}: {probabilidad:.2%}")

# Simulación de la carrera y mostrar resultado
ganador = simular_carrera(probabilidades)
st.header("Resultado")
st.markdown(f"<h1 style='text-align: center;'>¡El ganador es: <b>{ganador}</b>!</h1>", unsafe_allow_html=True)
