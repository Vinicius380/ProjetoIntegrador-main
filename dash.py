import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
from query import *
from Gemini.gemini import *
from datetime import datetime
from streamlit_modal import Modal
from graficos import *


st.set_page_config(
    page_title="Dashboard",  # título da página
    page_icon=":lizard:",  # ícone da página (opcional)
    layout="wide",  # ou "wide", se preferir layout mais amplo
    initial_sidebar_state='expanded'    #"collapsed"
)

# Consultas iniciais nas duas tabelas do banco
query = "SELECT * FROM tb_registro"
memoria = ("SELECT * FROM tb_memoria")

df = conexao(query)
df_memoria = conexao(memoria)

df['tempo_registro'] = pd.to_datetime(df['tempo_registro'])

df_selecionado = df.copy()   # Cria uma copia do df original.:

# ****************************** MENU LATERAL ******************************

st.sidebar.image("images/logo.png", use_container_width=True)

st.sidebar.markdown(f'<h1 style="text-transform: uppercase;">{'Selecione a região para gerar o gráfico'}</h1>', unsafe_allow_html=True)  

st.sidebar.subheader("Região")
SP = st.sidebar.checkbox("São Paulo", value=True)
ABC = st.sidebar.checkbox("Grade ABC", value=True)

if SP == False and ABC == False:
    st.sidebar.markdown(f'<p style="font-size:16px;font-weight:bold;background-color:#D3D4CD;display:flex;justify-content:center;padding:10px;border-radius:10px;">{"SELECIONE UMA REGIÃO!"}<p>', unsafe_allow_html=True)
    #st.sidebar.warning("Selecione uma região!")

# Lista de regiões selecionadas
regioes_selecionadas = []
if SP:
    regioes_selecionadas.append("São Paulo")
if ABC:
    regioes_selecionadas.append("Grande ABC")

# Filtrando o DataFrame com base nas regiões selecionadas
if regioes_selecionadas:
    df = df[df["regiao"].isin(regioes_selecionadas)]
    


# *********************************SLIDERS *****************************

# Verificar quais os atributos do filtro. 
# def filtros(atributo):
#     return atributo in [colunaX, colunaY]

# # Filtro de RANGE ==> SLIDER
# st.sidebar.header("Selecione o filtro")

# # UMIDADE
# if filtros("umidade"):
#     umidade_range = st.sidebar.slider(
#         "Umidade",
#         min_value = float(df["umidade"].min()),  # Valor Mínimo.
#         max_value = float(df["umidade"].max()),  # Valor Máximo.
#         value = (float(df["umidade"].min()), float(df["umidade"].max())),  # Faixa de Valores selecionado.
#         step = 0.1   # Incremento para cada movimento do slider.  
#     )

# # TEMPERATURA
# if filtros("temperatura"):
#     temperatura_range = st.sidebar.slider(
#         "Temperatura (°C)",
#         min_value = float(df["temperatura"].min()),  # Valor Mínimo.
#         max_value = float(df["temperatura"].max()),  # Valor Máximo.
#         value = (float(df["temperatura"].min()), float(df["temperatura"].max())),  # Faixa de Valores selecionado.
#         step = 0.1   # Incremento para cada movimento do slider. 
#     )

# # PRESSÃO
# if filtros("pressao"):
#     pressao_range = st.sidebar.slider(
#         "Pressao",
#         min_value = float(df["pressao"].min()),  # Valor Mínimo.
#         max_value = float(df["pressao"].max()),  # Valor Máximo.
#         value = (float(df["pressao"].min()), float(df["pressao"].max())),  # Faixa de Valores selecionado.
#         step = 0.1   # Incremento para cada movimento do slider. 
#     )

# # ALTITUDE
# if filtros("altitude"):
#     altitude_range = st.sidebar.slider(
#         "Altitude",
#         min_value = float(df["altitude"].min()),  # Valor Mínimo.
#         max_value = float(df["altitude"].max()),  # Valor Máximo.
#         value = (float(df["altitude"].min()), float(df["altitude"].max())),  # Faixa de Valores selecionado.
#         step = 0.1   # Incremento para cada movimento do slider. 
#     )

# # CO2
# if filtros("co2"):
#     co2_range = st.sidebar.slider(
#         "CO2",
#         min_value = float(df["co2"].min()),  # Valor Mínimo.
#         max_value = float(df["co2"].max()),  # Valor Máximo.
#         value = (float(df["co2"].min()), float(df["co2"].max())),  # Faixa de Valores selecionado.
#         step = 0.1   # Incremento para cada movimento do slider. 
#     )

# # POEIRA
# if filtros("poeira"):
#     poeira_range = st.sidebar.slider(
#         "Poeira",
#         min_value = float(df["poeira"].min()),  # Valor Mínimo.
#         max_value = float(df["poeira"].max()),  # Valor Máximo.
#         value = (float(df["poeira"].min()), float(df["poeira"].max())),  # Faixa de Valores selecionado.
#         step = 0.1   # Incremento para cada movimento do slider. 
#     )
# ## ************************************ FILTROS TEMPO_REGISTRO *************************************
# if filtros("tempo_registro"):
#     # Extrair as datas mínimas e máximas em formato de datetime
#     min_data = df["tempo_registro"].min()
#     max_data = df["tempo_registro"].max()

#     # Exibir dois campos de data para seleção de intervalo no sidebar
#     data_inicio = st.sidebar.date_input(
#         "Data de Início", 
#         min_data.date(), 
#         min_value=min_data.date(), 
#         max_value=max_data.date(),
#         format= "DD-MM-YYYY"
#     )
    
#     data_fim = st.sidebar.date_input(
#         "Data de Fim", 
#         max_data.date(), 
#         min_value=min_data.date(), 
#         max_value=max_data.date(),
#         format= "DD-MM-YYYY"
#     )

#     # Converter as datas selecionadas para datetime, incluindo hora
#     tempo_registro_range = (
#         pd.to_datetime(data_inicio),
#         pd.to_datetime(data_fim) + pd.DateOffset(days=1) - pd.Timedelta(seconds=1)
#     )

# if filtros("umidade"):
#     df_selecionado = df_selecionado[
#         (df_selecionado["umidade"] >= umidade_range[0]) &
#         (df_selecionado["umidade"] <= umidade_range[1])
#     ]

# if filtros("temperatura"):
#     df_selecionado = df_selecionado[
#         (df_selecionado["temperatura"] >= temperatura_range[0]) &
#         (df_selecionado["temperatura"] <= temperatura_range[1])
#     ]

# if filtros("pressao"):
#     df_selecionado = df_selecionado[
#         (df_selecionado["pressao"] >= pressao_range[0]) &
#         (df_selecionado["pressao"] <= pressao_range[1])
#     ]
    
# if filtros("altitude"):
#     df_selecionado = df_selecionado[
#         (df_selecionado["altitude"] >= altitude_range[0]) &
#         (df_selecionado["altitude"] <= altitude_range[1])
#     ]

# if filtros("co2"):
#     df_selecionado = df_selecionado[
#         (df_selecionado["co2"] >= co2_range[0]) &
#         (df_selecionado["co2"] <= co2_range[1])
#     ]

# if filtros("poeira"):
#     df_selecionado = df_selecionado[
#         (df_selecionado["poeira"] >= poeira_range[0]) &
#         (df_selecionado["poeira"] <= poeira_range[1])
#     ] 

# if filtros("tempo_registro"):
#     df_selecionado = df_selecionado[
#         (df_selecionado["tempo_registro"] >= tempo_registro_range[0]) &
#         (df_selecionado["tempo_registro"] <= tempo_registro_range[1])
#     ] 


# **************************** HOME****************************
    
def Home():
  
    # Título principal
    st.title("Dashboard de Monitoramento")

# ---------------------- APLICAÇÃO GEMINI -----------------------------------------------

    # Configuração do modal
    modal = Modal(
        "Análise Inteligente",
        key="gemini-modal",
        padding=40,
        max_width=744
    )

    # Botão para abrir o modal
    open_modal = st.button("Análise inteligente", icon='🤖', key="Analise")
    if open_modal:
        modal.open()

    # Configuração do conteúdo do modal
    if modal.is_open():
        with modal.container():
            st.write("Digite sua pergunta sobre a base de dados")
            user_input = st.text_area("Escreva algo aqui...", "")

            # Geração de conteúdo ao clicar em "Enviar"
            if st.button("Gerar análise"):
                if user_input.strip():
                    try:
                        
                        prompt = user_input
                        
                        resposta_gemini = gerar_resposta_gemini(df, df_memoria, prompt)
                        
                        st.write("Resposta da análise:")
                        st.write(resposta_gemini) 
                                
                        # Armazena o novo prompt e resposta na memória
                        save_to_memory(prompt, resposta_gemini)

                        print("Resposta gerada pelo Gemini:")
                        print(resposta_gemini)
                        
                    except Exception as e:
                        st.error(f"Ocorreu um erro ao acessar gerar resposta: {e}")
                else:
                    st.warning("Por favor, insira uma pergunta válida.")
            
            if st.button('Fechar'):
                modal.close()
            
# -------------------FIM DA APLICAÇÃO GEMINI ---------------------------------------------

    # Linha visível de delimitação
    st.markdown(
        """
        <hr style="
            border: none; 
            border-top: 2px solid #3E5050; /* Define a cor da linha */
            margin-top: 10px;             /* Espaçamento acima da linha */
            margin-bottom: 20px;          /* Espaçamento abaixo da linha */
        ">
        """,
        unsafe_allow_html=True
    )   

# **************************** MEDIAS****************************

    # Verifique se o DataFrame selecionado não está vazio
    if df_selecionado.empty:
        st.warning("Nenhum dado disponível para calcular as médias.")

    # Cálculo das médias
    media_umidade = df_selecionado["umidade"].mean()
    media_temperatura = df_selecionado["temperatura"].mean()
    media_co2 = df_selecionado["co2"].mean()

    # Layout em colunas para exibir as métricas
    col1, col2, col3 = st.columns(3)

    # Estilo personalizado para as caixas
    caixa_estilo = """
    <div style="
        background-color: #D3D4CD;
        border-radius: 10px;
        padding: 5px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        text-align: center;
    ">
        <h3 style="color: #215132; margin-bottom: 10px;">{titulo}</h3>
        <p style="font-size: 23px; font-weight: bold; margin: 0;">{valor}</p>
    </div>
    """

    # Exibição das caixas em cada coluna
    with col1:
        st.markdown(
            caixa_estilo.format(
                titulo="Média de Umidade", valor=f"{media_umidade:.2f}%"
            ),
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            caixa_estilo.format(
                titulo="Média de Temperatura", valor=f"{media_temperatura:.2f}°C"
            ),
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            caixa_estilo.format(
                titulo="Média de CO2", valor=f"{media_co2:.2f} ppm"
            ),
            unsafe_allow_html=True,
        )
        
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

# **************************** PLOTANDO GRÁFICOS ****************************
def graficos():
    
    if df_selecionado.empty:
        st.write("Nenhum dado está disponível para gerar gráficos")
        return
    else:
        col1, space, col2 = st.columns([10, 5, 10])

        with col1:
            grafico_barras(df_selecionado)
            grafico_linhas(df_selecionado)
        
        with col2:
            grafico_dispersao(df_selecionado)
            grafico_area(df_selecionado)
        
        grafico_barrasEmpilhadas(df_selecionado)

# **************************** CHAMANDO A FUNÇÃO ****************************
Home()
if SP == ABC == False:
    st.warning("Nenhum dado encontrado para os filtros selecionados!")
else:
    graficos()
    rodape_html = """
    <style>
    footer {
        position: relative; /* Permite que o rodapé seja colocado após o conteúdo */
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px 0;
        font-size: 14px;
        color: #333;
        
    }
    </style>
    <footer>
        <p>Copyright © 2024 - Todos os direitos reservados - Equipe Lagartixa</p>
    </footer>
    """
    st.markdown(rodape_html, unsafe_allow_html=True)