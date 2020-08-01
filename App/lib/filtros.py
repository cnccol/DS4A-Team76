###########################################################################
# importar librerias generales de dash
###########################################################################

import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate

###########################################################################
# importar librerias de manejo de archivos, operaciones y graficas
###########################################################################

import pathlib
import warnings
warnings.filterwarnings('ignore')

###########################################################################
# referenciamos py externos
###########################################################################

from app import app
from lib import consultas

###########################################################################
# creamos filtro de mapa
###########################################################################

filtro_01 = html.Div (children=[
                    html.Label('FILTRO MAPA', className='filtros-label')
                    ,dcc.Dropdown(
                        options=[
                            {'label': 'LLAMADAS EFECTIVAS', 'value': '1'}
                            ,{'label': 'DURACION LLAMADAS', 'value': '2'}
                            ,{'label': 'NUMERO DE CUOTAS', 'value': '3'}
                            ,{'label': 'PORC LLAMADAS EFECTIVAS', 'value': '4'}
                        ],id='id_flt_mapa_01',value='1')
                ],id='id_filtro_01',className='filtros')

###########################################################################
# creamos filtro de grafica
###########################################################################

filtro_1001 = html.Div (children=[
                    html.Label('TIPO_GRAFICO', className='filtros-label')
                    ,dcc.Dropdown(
                        options=[
                            {'label': 'BARRAS', 'value': '1'}
                            ,{'label': 'LINEAS', 'value': '2'}
                            ,{'label': 'SCATERPLOT', 'value': '3'}
                            ,{'label': 'BOXPLOT', 'value': '4'}
                        ],id='tipo_grafico_01',value='1')
                ],id='filtro_1001',className='filtros')

###########################################################################
# creamos filtro de slider de prueba por estrato
###########################################################################

filtro_02 = html.Div (children=[
                    html.Label('VARIABLE', className='filtros-label')
                    ,dcc.Dropdown(
                        options=[
                            {'label': 'Estrato', 'value': 'Estrato'}
                            ,{'label': 'Genero', 'value': 'Genero'}
                            ,{'label': 'Edad', 'value': 'Edad'}
                        ],id='id_efectivas_cuotas',value='Estrato')
                ],id='filtro_02',className='filtros')

###########################################################################
# creamos filtro de slider de prueba por estrato
###########################################################################

filtro_03 = html.Div (children=[
                    html.Label('TIEMPOS MARCADOR', className='filtros-label')
                    ,dcc.Dropdown(
                        options=[
                            {'label': 'Llamadas', 'value':'calls'},
                            {'label': 'Duración total', 'value': 'total'},
                            {'label': 'Duración espera', 'value': 'espera'},
                            {'label': 'Duración hablado', 'value': 'hablado'},
                            {'label': 'Duración disponible', 'value': 'disponible'},
                            {'label': 'Duración pausas', 'value': 'pausas'},
                            {'label': 'Duración muerto', 'value': 'muerto'},
                            {'label': 'Duración efectivas', 'value': 'duracion_efectivas'}
                        ],id='id_marcador',value='calls')
                ],id='filtro_03',className='filtros')

###########################################################################
# creamos filtro de Top 10 por año
###########################################################################

filtro_04 = html.Div (children=[
                    html.Label('AÑO', className='filtros-label')
                    ,dcc.Dropdown(
                        options=[
                            {'label': '2017', 'value': 2017},
                            {'label': '2018', 'value': 2018},
                            {'label': '2019', 'value': 2019},
                            {'label': '2020', 'value': 2020}
                        ],id='id_top_year',value=2020)
                ],id='filtro_04',className='filtros')

###########################################################################
# creamos filtro de Top 10 por mes
###########################################################################

filtro_05= html.Div (children=[
                    html.Label('MES', className='filtros-label')
                    ,dcc.Dropdown(
                        options=[
                            {'label': 'Enero', 'value':1},
                            {'label': 'Febrero', 'value':2},
                            {'label': 'Marzo', 'value':3},
                            {'label': 'Abril', 'value':4},
                            {'label': 'Mayo', 'value':5},
                            {'label': 'Junio', 'value':6},
                            {'label': 'Julio', 'value':7},
                            {'label': 'Agosto', 'value':8},
                            {'label': 'Septiembre', 'value':9},
                            {'label': 'Octubre', 'value':10},
                            {'label': 'Noviembre', 'value':11},
                            {'label': 'Diciembre', 'value':12}
                        ],id='id_top_mes',value=3)
                ],id='filtro_05',className='filtros')


###########################################################################
# creamos filtro de slider para modificar por mes los markdown
###########################################################################

filtro_06 = html.Div (children=[
                    html.Label('DURACIÓN [MESES]', className='filtros-label')
                    ,dcc.Slider(
                        id='my-slider',
                        min=1,
                        max=26,
                        step=1,
                        value=6,
                        #mark={1:'1', 2:'2', 3:'3', 4:'4', 5:'5',6:'6'},
                    ), html.Div(id='id_filtro_06')
                ],id='filtro_06',className='filtros')


