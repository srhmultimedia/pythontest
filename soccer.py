import streamlit as st
import random

# Datos de los equipos
francia_rio = {"ganados": 3, "empatados": 1, "perdidos": 2, "goles_a_favor": 11, "goles_en_contra": 10}
francia_tokio = {"ganados": 2, "empatados": 1, "perdidos": 2, "goles_a_favor": 9, "goles_en_contra": 10}
colombia_rio = {"ganados": 1, "empatados": 2, "perdidos": 2, "goles_a_favor": 5, "goles_en_contra": 7}
colombia_tokio = {"ganados": 0, "empatados": 1, "perdidos": 3, "goles_a_favor": 7, "goles_en_contra": 10}

# Calcular la puntuación para cada equipo
def calcular_puntuacion(equipo):
    partidos_jugados = equipo["ganados"] + equipo["empatados"] + equipo["perdidos"]
    puntos_partidos = (equipo["ganados"] * 3 + equipo["empatados"] * 1) / partidos_jugados
    puntos_goles = (equipo["goles_a_favor"] - equipo["goles_en_contra"]) / partidos_jugados
    puntuacion = puntos_partidos + puntos_goles
    return puntuacion

# Calcular las puntuaciones
puntuacion_francia = calcular_puntuacion(francia_rio) + calcular_puntuacion(francia_tokio)
puntuacion_colombia = calcular_puntuacion(colombia_rio) + calcular_puntuacion(colombia_tokio)

# Calcular probabilidades
total_puntuaciones = puntuacion_francia + puntuacion_colombia
probabilidad_francia = puntuacion_francia / total_puntuaciones
probabilidad_colombia = puntuacion_colombia / total_puntuaciones

# Simulación del partido
def simular_partido(probabilidad_francia, probabilidad_colombia):
    resultado = random.choices(
        population=["Francia", "Colombia"],
        weights=[probabilidad_francia, probabilidad_colombia],
        k=1
    )
    return resultado[0]

# Frontend con Streamlit
st.title("Simulación de Partido: Francia vs Colombia")

st.header("Estadísticas de los Equipos")
st.subheader("Francia:")
st.write(f"- Puntuación: {puntuacion_francia:.2f}")
st.write(f"- Probabilidad de ganar: {probabilidad_francia:.2%}")

st.subheader("Colombia:")
st.write(f"- Puntuación: {puntuacion_colombia:.2f}")
st.write(f"- Probabilidad de ganar: {probabilidad_colombia:.2%}")

# Simulación del partido y mostrar resultado
resultado = simular_partido(probabilidad_francia, probabilidad_colombia)
st.header("Resultado del Partido")
st.markdown(f"<h1 style='text-align: center;'>¡Ganador: <b>{resultado}</b>!</h1>", unsafe_allow_html=True)
