import streamlit as st
import pandas as pd
import numpy as np

# Función para calcular D'Hondt
def dhont(votos, bancas):
    partidos = list(votos.keys())
    cocientes = {p: [] for p in partidos}
    resultados = {p: 0 for p in partidos}
    
    for _ in range(bancas):
        for p in partidos:
            cocientes[p] = votos[p] / (resultados[p] + 1)
        ganador = max(cocientes, key=cocientes.get)
        resultados[ganador] += 1
    
    return resultados

# Interfaz en Streamlit
st.title("Simulador D'Hondt")



porcentaje = st.number_input("Calcula la cantidad de votos", min_value=0.0, max_value=100.0, value=10.0, step=0.1)

# Cálculo de votos
total_votos = 1_800_000
votos_calculados = (porcentaje / 100) * total_votos

st.write(f"🔹 {porcentaje}% de {total_votos:,} votos es **{int(votos_calculados):,} votos**")

# Input para votos de 6 fuerzas políticas
fuerzas = ["LLA", "UXP", "PRO", "HORACIO", "OTRA FUERZA 1", "OTRA FUERZA 2"]
votos = {}

for f in fuerzas:
    votos[f] = st.number_input(f, min_value=0, value=10000, step=1000)

bancas_totales = 30

if st.button("Calcular Bancas"):
    resultado = dhont(votos, bancas_totales)
    df_resultados = pd.DataFrame(list(resultado.items()), columns=["Fuerza", "Bancas Obtenidas"])
    
    # Mostrar tabla con los resultados
    st.write("### Distribución de Bancas")
    st.dataframe(df_resultados)

