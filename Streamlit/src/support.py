import pandas as pd
import plotly.express as px

def plot_plotly():
    # Lee el csv con mi dataframe
    df = pd.read_csv('../data/df_scaled.csv')

    # Crea la figura de Plotly
    fig = px.line(df, x='date', y=['Precipitaciones Medias Diarias', 'Audiencia Diaria'])

    # Esconde los títulos de los ejes
    fig.update_yaxes(title_text=None)
    fig.update_xaxes(title_text=None)

    # Esconde los números del eje y
    fig.update_layout(yaxis=dict(tickfont=dict(color='rgba(0,0,0,0)')))

    # Devuelve la figura
    return fig

def call_csv(ruta):
    df_merged2_date = pd.read_csv(ruta,index_col= 0)
    return df_merged2_date

def plot_histplot(df,date,column):

    filtered_data = df[df["date"] == date]
    # Crea el histograma con plotly
    fig = px.histogram(filtered_data, y='revenue_resold', x= column)

    # Esconde los títulos de los ejes
    fig.update_yaxes(title_text=None)
    fig.update_xaxes(title_text=None)

    # Quita las labels del eje y
    fig.update_layout(yaxis=dict(title=None))

    # Quita los ticks del eje y
    fig.update_yaxes(showticklabels=False)

    # Devuelve la figura
    return fig
