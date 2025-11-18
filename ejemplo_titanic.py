import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carga el archivo CSV "database_titanic.csv" en un DataFrame de pandas.
df = pd.read_csv("database_titanic.csv")

# Muestra un título y una descripción en la aplicación Streamlit.
st.write("""
# ACCIDENTE EN EL TITANIC
## datos proporcionados 
""")

# Usando la notación "with" para crear una barra lateral en la aplicación Streamlit.
with st.sidebar:
    st.write("# Opciones")
    div = st.slider('Número de bins:', 0, 10, 2)
    st.write("Bins=", div)

# --- Gráficos de edades y distribución por sexo ---
fig, ax = plt.subplots(1, 2, figsize=(10, 3))

# Histograma de edades
ax[0].hist(df["Age"], bins=div, color="green" )
ax[0].set_xlabel("Edad")
ax[0].set_ylabel("Frecuencia")
ax[0].set_title("Histograma de edades")

# Conteo de hombres y mujeres
df_male = df[df["Sex"] == "male"]
cant_male = len(df_male)

df_female = df[df["Sex"] == "female"]
cant_female = len(df_female)

ax[1].bar(["Masculino", "Femenino"], [cant_male, cant_female], color=["yellow","purple"])
ax[1].set_xlabel("Sexo")
ax[1].set_ylabel("Cantidad")
ax[1].set_title('Distribución de hombres y mujeres')

st.pyplot(fig)

# -----------------------------
# NUEVO GRÁFICO: SOBREVIVIENTES SEPARADOS POR SEXO
# -----------------------------

st.write("## Personas con vida")

# Agrupar por sexo y sobrevivencia (Survived = 1)
survivors = df[df["Survived"] == 1].groupby("Sex").size()

# Preparar datos
labels = ["hombre", "mujer"]
values = [survivors.get("male", 0), survivors.get("female", 0)]

# Crear figura
fig2, ax2 = plt.subplots(figsize=(5, 3))
ax2.bar(labels, values, color=["yellow", "red"])
ax2.set_xlabel("Sexo ")
ax2.set_ylabel("Cantidad de sobrevivientes")
ax2.set_title("Sobrevivientes separados por sexo")

st.pyplot(fig2)
# -----------------------------

st.write("""
## Resultado de los datos proporcionados
""")

# Graficamos una tabla
st.table(df.head())
