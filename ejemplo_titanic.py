import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carga el archivo CSV "database_titanic.csv" en un DataFrame de pandas.
df = pd.read_csv("database_titanic.csv")

# Muestra un título y una descripción en la aplicación Streamlit.
st.write("""
# Mi primera app 
## Graficos generados con la info del titanic
""")

# Usando la notación "with" para crear una barra lateral en la aplicación Streamlit.
with st.sidebar:
    # Título para la sección de opciones en la barra lateral.
    st.write("# Opciones")
    
    # Crea un control deslizante (slider) que permite al usuario seleccionar un número de bins
    # en el rango de 0 a 10, con un valor predeterminado de 2.
    div = st.slider('Número de bins:', 0, 10, 2)
    
    # Muestra el valor actual del slider en la barra lateral.
    st.write("Bins=", div)

# Desplegamos un histograma con los datos del eje X
fig, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].hist(df["Age"], bins=div, colors="green" )
ax[0].set_xlabel("Edad")
ax[0].set_ylabel("Frecuencia")
ax[0].set_title("Distribucion de edades")

# Tomando datos para hombres y contando la cantidad
df_male = df[df["Sex"] == "male"]
cant_male = len(df_male)

# Tomando datos para mujeres y contando la cantidad
df_female = df[df["Sex"] == "female"]
cant_female = len(df_female)

ax[1].bar(["Masculino", "Femenino"], [cant_male, cant_female], color=["brown","yellow"])
ax[1].set_xlabel("Sexo")
ax[1].set_ylabel("Cantidad")
ax[1].set_title('Distribución de hombres y mujeres')

# Desplegamos el gráfico
st.pyplot(fig)
st.write("## personas que sobrevivieron")

# Agrupar por sexo y sobrevivencia (Survived = 1)
survivors = df[df["Survived"] == 1].groupby("Sex").size()

# Preparar datos
labels = ["Masculino", "femenino"]
values = [survivors.get("male", 0), survivors.get("female", 0)]

# Crear figura
fig2, ax2 = plt.subplots(figsize=(5, 3))
ax2.bar(labels, values)
ax2.set_xlabel("Sexo ")
ax2.set_ylabel("Cantidad de sobrevivientes")
ax2.set_title("Sobrevivientes separados por sexo")

st.pyplot(fig2)

st.write("""
## Muestra de datos cargados
""")
# Graficamos una tabla
st.table(df.head())
