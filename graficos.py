import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
from query import *
from datetime import datetime
from streamlit_modal import Modal

def grafico1(df_selecionado):
    # Grafico 1
    # Seleção da coluna X  |  selectbox ==> Cria uma caixa de seleção na barra lateral. 
    colunaX = st.selectbox(
        "Eixo X",
        options = ["umidade", "temperatura", "pressao", "altitude", "co2", "poeira", "tempo_registro"],
        index = 0,
        key='eixox1'
    )
    
    try:           
        grupo_dados1 = df_selecionado.groupby(by=[colunaX]).size().reset_index(name="contagem")
        fig_valores = px.bar(
            grupo_dados1,       # De onde vem os dados.
            x = colunaX,        # Eixo X
            y = "contagem",     # Eixo Y com o nome que nós renomeamos no GrupBy
            orientation = "v",  # Orientação do Gráfico
            title = f"Contagem de Registros por {colunaX.capitalize()}", # Titulo do gráfico => A função capitalize() deixa tudo em maiúsculo. 
            color_discrete_sequence = ["#455354"],       # Altera a cor 
            template = "plotly_white"
        )
        
    except Exception as e:
        st.error(f"Erro ao criar gráfico de barras:  {e}")
    st.plotly_chart(fig_valores, use_container_width=True)
    
def grafico2(df_selecionado):
    # Grafico 2
    # Seleção da coluna X  |  selectbox ==> Cria uma caixa de seleção na barra lateral. 
    colunaX = st.selectbox(
        "Eixo X",
        options = ["umidade", "temperatura", "pressao", "altitude", "co2", "poeira", "tempo_registro"],
        index = 0,
        key='eixox2'
    )

    # Seleção da coluna Y  |  selectbox ==> Cria uma caixa de seleção na barra lateral. 
    colunaY = st.selectbox(
        "Eixo Y",
        options = ["umidade", "temperatura", "pressao", "altitude", "co2", "poeira", "tempo_registro"],
        index = 1,
        key='eixoy2'
    )
    
    if colunaX == colunaY:
        st.warning("Selecione uma opção diferente para os eixos X e Y")
        return
    
    try:           
        grupo_dados2 = df_selecionado.groupby(by=[colunaX])[colunaY].mean().reset_index(name=colunaY)
        fig_valores2 = px.line(
            grupo_dados2,
            x=colunaX,
            y=colunaY,
            title=f"Gráfico de Linhas: {colunaX.capitalize()} vs {colunaY.capitalize()}",
            line_shape='linear',  # Tipo de linha
            markers=True  # Para mostrar marcadores nos pontos
        )   
        
        fig_valores2.update_traces(line_color="#455354")
        
    except Exception as e:
        st.error(f"Erro ao criar gráfico de barras:  {e}")
    st.plotly_chart(fig_valores2, use_container_width=True)
    
def grafico3(df_selecionado):
    # Grafico 3
    # Seleção da coluna X  |  selectbox ==> Cria uma caixa de seleção na barra lateral. 
    colunaX = st.selectbox(
        "Eixo X",
        options = ["umidade", "temperatura", "pressao", "altitude", "co2", "poeira", "tempo_registro"],
        index = 0,
        key='eixox3'
    )

    # Seleção da coluna Y  |  selectbox ==> Cria uma caixa de seleção na barra lateral. 
    colunaY = st.selectbox(
        "Eixo Y",
        options = ["umidade", "temperatura", "pressao", "altitude", "co2", "poeira", "tempo_registro"],
        index = 1,
        key='eixoy3'
    )
    
    if colunaX == colunaY:
        st.warning("Selecione uma opção diferente para os eixos X e Y")
        return
    try:
        grupo_dados3 = df_selecionado.groupby(by=[colunaX]).size().reset_index(name=colunaY)
        fig_valores3 = px.scatter(grupo_dados3, x = colunaX, y = colunaY)  
        fig_valores3.update_traces(marker_color="#455354")
        fig_valores3.update_traces(marker_color="#455354", marker_size=10, marker_symbol="circle")  
        
        st.plotly_chart(fig_valores3, use_container_width=True)
            
    except Exception as e:
        st.error(f"Erro ao criar gráfico de dispersão: {e}")
        
def grafico4(df_selecionado):
    # Grafico 3
    # Seleção da coluna X  |  selectbox ==> Cria uma caixa de seleção na barra lateral. 
    colunaX = st.selectbox(
        "Eixo X",
        options = ["umidade", "temperatura", "pressao", "altitude", "co2", "poeira", "tempo_registro"],
        index = 0,
        key='eixox4'
    )

    # Seleção da coluna Y  |  selectbox ==> Cria uma caixa de seleção na barra lateral. 
    colunaY = st.selectbox(
        "Eixo Y",
        options = ["umidade", "temperatura", "pressao", "altitude", "co2", "poeira", "tempo_registro"],
        index = 1,
        key='eixoy4'
    )
    
    if colunaX == colunaY:
        st.warning("Selecione uma opção diferente para os eixos X e Y")
        return
    try:
        grupo_dados4 = df_selecionado.groupby(by=[colunaX]).size().reset_index(name=colunaY)
        st.area_chart(grupo_dados4, x = colunaX, y = colunaY, color= ["#455354"], stack="center" )

    except Exception as e:
        st.error(f"Erro ao criar gráfico de dispersão: {e}")
        
def grafico5(df_selecionado):
    # Grafico 5
    # Seleção da coluna X  |  selectbox ==> Cria uma caixa de seleção na barra lateral. 
    colunaX = st.selectbox(
        "Eixo X",
        options = ["umidade", "temperatura", "pressao", "altitude", "co2", "poeira", "tempo_registro"],
        index = 0,
        key='eixox5'
    )

    # Seleção da coluna Y  |  selectbox ==> Cria uma caixa de seleção na barra lateral. 
    colunaY = st.selectbox(
        "Eixo Y",
        options = ["umidade", "temperatura", "pressao", "altitude", "co2", "poeira", "tempo_registro"],
        index = 1,
        key='eixoy5'
    )
    
    if colunaX == colunaY:
        st.warning("Selecione uma opção diferente para os eixos X e Y")
        return
    try:
        grupo_dados5 = df_selecionado
        
        cores_personalizadas = {
            'São Paulo': '#455354',  # Cor para a região Norte
            'Grande ABC': '#77A074'    # Cor para a região Sul
        }
    
        fig_barra = px.bar(grupo_dados5, 
                            x=colunaX,
                            y=colunaY,
                            color='regiao',
                            barmode='group',
                            title='Comparação entre regiões',
                            color_discrete_map= cores_personalizadas
                            )
        
        st.plotly_chart(fig_barra, use_container_width=True)
    
    except Exception as e:
        print(f'Erro ao criar o gráfico: {e}')