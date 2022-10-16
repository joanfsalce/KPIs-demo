from email.policy import default
from ssl import Options
from unittest.mock import DEFAULT
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="KPIs Transaccionales",
    page_icon=":bowtie:",
    layout="centered")

st.title("Kpis Data Transaccional :chart_with_upwards_trend:")
st.subheader("Suba su documento de extensión (.csv)")


uploaded_file = st.file_uploader("Suba su CSV", accept_multiple_files=False, key="data")


if uploaded_file is not None:
    @st.cache(allow_output_mutation=True)
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    st.write("---")
    st.subheader("Visualización Previa")
    st.write(df.head(2))
    st.write("---")
    
    st.subheader("Seleccione la columna correspondiente")

    opciones = list(df.columns)
    col1, col2 = st.columns(2)
    with col1:

        factura = st.selectbox("Columna de factura", opciones, key="factura")
        st.write(f"Usted ha elegido:", factura)

        producto = st.selectbox("Columna de producto", opciones, key="producto")
        st.write(f"Usted ha elegido:", producto)

        cantidad = st.selectbox("Columna de cantidad", opciones, key="cantidad")
        st.write(f"Usted ha elegido:", cantidad)
    with col2:
        precio = st.selectbox("Columna de precio", opciones, key="precio")
        st.write(f"Usted ha elegido:", precio)

        pais = st.selectbox("Columna de pais", opciones, key="pais")
        st.write(f"Usted ha elegido:", pais)

    if factura == pais:
        st.info("No puede seleccionar columnas duplicadas") 
    else:
        st.success("Columnas Seleccionadas")
    
        if st.button("Generar Indicadores"):
            st.write("---")
            st.subheader("Indicadores")

            # Ticket_Promedio = df['total_value'].sum() / df[factura].nunique()
            Canasta_Media = df[cantidad].sum() / df[factura].nunique()
            col3, col4, col5 = st.columns(3)
            with col3:
                st.metric(label="Cantidades Vendidas", value=df[cantidad].sum())

            with col4:
                st.metric(label="Facturas Unicas", value=df[factura].nunique())
                # df[total_value] = df[cantidad] * df[precio]
                # st.metric(label="Revenue", value=int(df[total_value].sum()))

            with col5:
                st.metric(label="Canasta Media", value= round(Canasta_Media, 2))
                # st.metric(label="Ticket Promedio", value=round(Ticket_Promedio, 2))
                # st.metric(label="Precio Promedio por Item", value=round((Ticket_Promedio / Canasta_Media), 2))

    



else: 

    st.info('Esperando la carga de documentos')
    st.write("---")
    st.subheader(":point_down: O puede descargar el archivo de prueba :point_down:")
    st.caption ("1. Haga click derecho y seleccione guardar enlace como")
    st.caption ("2. Coloquele un nombre seguido de (.csv)")

    st.caption("""
    [Archivo de prueba](https://raw.githubusercontent.com/joanfsalce/KPIs-demo/main/Online_Retail.csv)
    """)
    
    
