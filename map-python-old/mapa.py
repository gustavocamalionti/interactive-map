import folium
from folium.plugins import Fullscreen
from folium.plugins import MarkerCluster
import pandas as pds

# IMPORTANDO A PLANILHA COM DADOS
ler = pds.read_excel(r'D:\Projetos\jinjin\interactive-map\dados\dadosmap.xlsx')

# MAPA: CONFIGURAÇÕES GERAIS
mapa = folium.Map(
    location=[-13.7048968, -69.6590157],
    world_copy_jump=True,
    tiles='OpenStreetMap',
    zoom_start=3,
)

# BOTÃO DE FULLSCREEN
Fullscreen(
    position='topright',
    title='Entrar/Sair da Tela Cheia',
    title_cancel='Sair da Tela Cheia',
    force_separate_button=True).add_to(mapa)

# INTERAÇÕES ENTRE OS MARCADORES.
for index, linha in ler.iterrows():
    cluster = MarkerCluster().add_to(mapa)

print(ler)
# CRIANDO O LOOP
for index, linha in ler.iterrows():
    folium.Marker(
        location=[linha['LAT'], linha['LONG']],
        popup='<div class="btn btn-success">TESTE<hr></div>',
        tooltip="clique aqui!",
        icon=folium.Icon(color="red", icon="info-sign")
        
       
        ).add_to(cluster)

# folium.CircleMarker(location=[-23.8641866,-46.4303154], radius=25, popup='<b>SANTOS</b>', color='#3186cc', fill=True, fill_color='#3186cc').add_to(cluster)
minimap = folium.plugins.MiniMap()
mapa.add_child(minimap)
# BOTÃO DE CONTROLE "ESTADOS"
# folium.LayerControl().add_to(mapa)
mapa.save(r'D:\Projetos\jinjin\interactive-map\mapa.html')
