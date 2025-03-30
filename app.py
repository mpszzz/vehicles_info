import plotly_express as px
import pandas as pd
import streamlit as st

st.title("Análisis de Datos de Vehículos")  
st.write("Explora la distribución del odómetro y la relación entre odómetro y precio con gráficos interactivos.")

car_data = pd.read_csv("vehicles_us.csv")  

if car_data is not None:  
    if st.button('Construir histograma'):  
        st.write('Creación de un histograma del odómetro')  
        fig = px.histogram(car_data, x="odometer")  
        st.plotly_chart(fig, use_container_width=True)  

    if st.button('Construir gráfico de dispersión'):  
        st.write('Gráfico de dispersión: Odómetro vs Precio')  
        fig = px.scatter(car_data, x="odometer", y="price")  
        st.plotly_chart(fig, use_container_width=True)  
