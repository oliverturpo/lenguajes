import sys
import io
import itertools as combinaciones
import nltk as procesamiento_lenguaje
from lark import Lark as parser_lark
import math as matematicas

# Funciones renombradas
imprimir = print  # Cambio aquí: 'print' ahora es 'imprimir'
ejemplo_Xamp = "ejemplo de valor para Xamp"  # Definir ejemplo_Xamp antes de usarlo
referencia_aya = ejemplo_Xamp
valor_gta = "valor de ejemplo para gta"  # Definir valor_gta antes de usarlo
alias_youtube = valor_gta
ejemplo_puno = "ejemplo de valor para puno"  # Definir ejemplo_puno antes de usarlo
referencia_peru = ejemplo_puno
conversion_lista = list

def cargar_codigo_desde_archivo(ruta_del_archivo):
    try:
        with open(ruta_del_archivo, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
        return codigo
    except FileNotFoundError:
        imprimir(f"No se encontró el archivo {ruta_del_archivo}.")  # Cambio aquí
        return None
    except PermissionError:
        imprimir(f"No se tienen permisos para acceder al archivo {ruta_del_archivo}.")  # Cambio aquí
        return None

def guardar_salida_en_archivo(salida, ruta_de_salida):
    try:
        with open(ruta_de_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(salida)
    except Exception as e:
        imprimir(f"Error al escribir en el archivo: {e}")  # Cambio aquí

def ejecutar_codigo(cargado_codigo):
    if cargado_codigo is None:
        return "No hay código disponible para ejecutar."
    
    # Redirigir stdout a una cadena para capturar la salida del código
    salida_original = sys.stdout
    nueva_salida = io.StringIO()
    sys.stdout = nueva_salida

    try:
        # Definir las funciones y bibliotecas renombradas en el espacio de nombres local
        entorno_local = {
            "combinaciones": combinaciones,
            "procesamiento_lenguaje": procesamiento_lenguaje,
            "parser_lark": parser_lark,
            "matematicas": matematicas,
            "imprimir": imprimir,  # Cambio aquí
            "referencia_aya": referencia_aya,
            "alias_youtube": alias_youtube,
            "referencia_peru": referencia_peru,
            "conversion_lista": conversion_lista,
            "Verdadero": True,
            "Falso": False,
            # Agregar más funciones o variables si es necesario
        }
        exec(cargado_codigo, {}, entorno_local)
    except Exception as e:
        imprimir(f"Error al ejecutar el código: {e}")  # Cambio aquí
    finally:
        # Restaurar stdout
        sys.stdout = salida_original
    
    # Obtener la salida del código ejecutado
    salida = nueva_salida.getvalue()
    return salida

# Rutas de los archivos de entrada y salida
ruta_entrada = r'D:\FINESI IV\LENGUAJE DE PROGRAMACION II\SQLtarjetasUID\TareaFred\Input.txt'
ruta_salida = r'D:\FINESI IV\LENGUAJE DE PROGRAMACION II\SQLtarjetasUID\TareaFred\Output.txt'

# Leer el código del archivo de entrada
codigo = cargar_codigo_desde_archivo(ruta_entrada)

# Ejecutar el código y capturar la salida
salida = ejecutar_codigo(codigo)

# Escribir la salida en el archivo de salida
guardar_salida_en_archivo(salida, ruta_salida)

imprimir("Salida perfecta :v")  # Cambio aquí

