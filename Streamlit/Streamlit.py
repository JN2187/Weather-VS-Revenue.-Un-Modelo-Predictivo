import streamlit as st
import pandas as pd
import datetime
import io
from dateutil.relativedelta import relativedelta
import src.support as sp
import h2o
from h2o.automl import H2OAutoML
# inicializar H2O
h2o.init()

st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title='comparison', page_icon=":cloud:")


st.title("Weather VS Revenue. Un Modelo Predictivo")

st.markdown('En este proyecto de análisis de datos, he llevado a cabo una investigación para demostrar la hipótesis de que la audiencia de un site weather, está vinculada a la inestabilidad climática, en concreto a las precipitaciones. Se han cruzado y analizado datos del 2022 de las precipitaciones en la península, la audiencia en el site, y los clientes que más han invertido en campañas Programáticas (Compra de campañas de publicidad en Marketplaces, donde se llevan a cabo subastas digitales de los espacios publicitarios), analizando los formatos que mejor funcionan en sus campañas. Y a través de un modelo de Machine Learning y juntando todas éstas variables, se ha generado un modelo que tiene la capacidad de estimar el Revenue que podría generar un cliente bajo unas condiciones específicas, pudiendo optimizar los costes de las campañas para generar aún más revenue')

col1, col2= st.columns([8,2])
with col1:
    st.markdown('**Audiencia VS Precipitaciones 2022**')
    st.plotly_chart(sp.plot_plotly(),use_container_width=True)
with col2:
    data = sp.call_csv(ruta='../data/merged_df_2022_date.csv')
    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d').dt.date
    selected_date = st.date_input("**Selecciona un periodo**", datetime.date(2022, 2, 1))

    # Calculate the previous month from the selected date
    previous_month = (selected_date - relativedelta(months=1)).replace(day=1)

    # Filtra la fecha seleccionada en mi df por la columna date
    filtered_data = data[data["date"] == selected_date]

    # Filtra la fecha del mes anterior
    filtered_data_previous = data[data["date"] == previous_month]

    if not filtered_data.empty:
        # Mostrar las métricas de los datos filtrados
        st.metric(label="**Precipitaciones Medias Diarias**", value=f"{(filtered_data['media_prec'].round(2).iloc[0]):.2f} mm", delta=f"{(filtered_data['media_prec'].round(2).iloc[0] - filtered_data_previous['media_prec'].round(2).iloc[0]):.2f} mm")
        st.metric(label="**Audiencia Diaria**", value=f"{(filtered_data['sessions'].round(2).iloc[0] / 1000000):.2f} M", delta=f"{((filtered_data['sessions'].round(2).iloc[0] - filtered_data_previous['sessions'].round(2).iloc[0]) / 1000000):.2f} M")
        st.metric(label="**Revenue**", value=f"{(filtered_data['revenue_resold'].round(2).iloc[0] / 1000):.2f} K €", delta=f"{((filtered_data['revenue_resold'].round(2).iloc[0] - filtered_data_previous['revenue_resold'].round(2).iloc[0]) / 1000):.2f} K €")
    else:
        st.warning(f"No se encontraron datos para la fecha seleccionada: {selected_date}")

col3, col4= st.columns([3,3])
with col3:
    data2 = sp.call_csv(ruta='../data/merged_df_2022_formatos.csv')
    data2['date'] = pd.to_datetime(data2['date'], format='%Y-%m-%d').dt.date # Filtra la fecha seleccionada en mi df por la columna date
    st.markdown(f'**Mejores Formatos {selected_date}**')
    filtered_data2 = data2[data2["date"] == selected_date]
    st.plotly_chart(sp.plot_histplot(data2,selected_date,'format_name'),use_container_width=True)
with col4:
    data3 = sp.call_csv(ruta='../data/merged_df_2022_brand_name.csv')
    data3['date'] = pd.to_datetime(data2['date'], format='%Y-%m-%d').dt.date # Filtra la fecha seleccionada en mi df por la columna date
    data3 = data3.rename(columns={'revenue_resold': 'Revenue', 'brand_id_name': 'Cliente','date':'Fecha'})
    data3['Revenue'] = data3['Revenue'].apply(lambda x: f"{(x / 1000):.2f} K €")
    st.markdown(f'**Mejores Clientes {selected_date}**')
    filtered_data2 = data3[data3["Fecha"] == selected_date].reset_index(drop=True)
    # st.plotly_chart(sp.plot_histplot(data3,selected_date,'brand_id_name'),use_container_width=True)
    st.table(filtered_data2.head(10))

 
loaded_model = h2o.load_model("../data/best_model_3/DeepLearning_grid_2_AutoML_2_20230421_201630_model_1")


# Check if a file has been uploaded
uploaded_file = st.file_uploader("Selecciona un CSV", type='csv')


if uploaded_file is None:

    st.write("Carga un Archivo")

else:

    
    for upload in uploaded_file:
        bytes_data = uploaded_file.read()
        st.write(bytes_data)
    new_data = h2o.import_file("../data/df_test.csv")


    # Hacer predicciones en los nuevos datos utilizando el modelo cargado
    predictions = loaded_model.predict(new_data)

    predictions_df = predictions.as_data_frame()


    resultado = predictions_df['predict'][0].round(2)

    col6, col7, col8 = st.columns([6,3,4])
    with col6:
        st.markdown('')
    with col7:
    # Muestra la Predicción
        st.metric(label="**Predicción del Revenue**", value=f"{(resultado / 1000):.2f} K €")
    with col8:
        st.markdown('')


