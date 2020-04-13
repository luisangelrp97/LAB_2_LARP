
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: Microestructura y Sistemas de Trading - Laboratorio 2 - Behavioral Finance
# -- archivo: visualizaciones.py - para visualizacion de datos
# -- mantiene: Luis Angel Ruiz 
# -- repositorio: https://github.com/luisangelrp97/LAB_2_LARP
# -- ------------------------------------------------------------------------------------ -- #
# -- --------------------------------------------------------- GRÁFICA: df_1_ranking -- #
# -- ------------------------------------------------------------------------------------ -- #
# -- --- Grafica de efectividad de los insturmentos

import matplotlib.pyplot as plt
def df_1_ranking(f_estadisticas):
    labels = f_estadisticas['Efectividad']['symbol']
    sizes =  f_estadisticas['Efectividad']['profit']
    sizes = list(map(lambda sizes: sizes.replace("%",""), sizes))
    explode = (0, 0.1, 0.1, 0,0,0,0,0,0,0,0)
    plt.pie(sizes, explode=explode, labels = labels, shadow=True, startangle=140)
    plt.title('Ranking')
    plt.legend(loc = (1.3,.2))
    plt.xlabel('efectividad por instrumento')
    plt.show()
