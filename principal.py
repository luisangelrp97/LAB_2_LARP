
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: Microestructura y Sistemas de Trading - Laboratorio 2 - Behavioral Finance
# -- archivo: principal.py - flujo principal del proyecto
# -- mantiene: Luis Angel Ruiz 
# -- repositorio: https://github.com/luisangelrp97/LAB_2_LARP
# -- ------------------------------------------------------------------------------------ -- #
import funciones as fn


archivo = "archivo_tradeview_1.xlsx"
df_archivo = fn.f_leer_archivo(archivo)
datos = df_archivo
datos = fn.f_columnas_tiempos(datos)
datos = fn.f_columnas_pips(datos)
datos = fn.capital_acm(datos)

f_estadisticas = fn.f_estadisticas_ba(datos)
profit_diario = fn.f_profit_diario(datos)

vi.df_1_ranking(f_estadisticas)