import pandas as pd
from sodapy import Socrata

def obtener_datos_suelos(Departamento, Municipio, Cultivo, limite):
    """
    Returns:
        pd.DataFrame: DataFrame con los datos obtenidos de la API o None si hubo un error.
    """
    if not isinstance(Departamento, str) or not isinstance(Municipio, str) or not isinstance(Cultivo, str):
        raise ValueError("Los parámetros 'Departamento', 'Municipio' y 'Cultivo' deben ser cadenas de texto.")
    if not isinstance(limite, int) or limite <= 0:
        raise ValueError("El parámetro 'limite' debe ser un entero positivo.")
    
    try:
        client = Socrata("www.datos.gov.co", None)
        
        # Realizar la consulta a la API con filtros específicos
        query = f"Departamento='{Departamento}' AND Municipio LIKE '%{Municipio}%' AND Cultivo='{Cultivo}'"
        resultados = client.get("ch4u-f3i5", where=query, limit=limite)
        
        # Convertir los resultados a un DataFrame de pandas
        resultados_df = pd.DataFrame.from_records(resultados)

        if resultados_df.empty:
            print("No se pudo encontrar los datos para los criterios especificados.")
            return None
        
        # No imprimir columnas en consola
        # print("Columnas disponibles en el DataFrame:", resultados_df.columns)
        
        return resultados_df

    except Exception as e:
        print(f"Se presentó un error al obtener los datos: {e}")
        return None

def calcular_mediana_variables_edaficas(resultados_df):
    """
    Calcula la mediana de las variables edáficas (pH, Fósforo, Potasio) del DataFrame,
    ignorando los valores NaN y valores no numéricos.

    Args:
        resultados_df (pd.DataFrame): DataFrame con los resultados obtenidos de la API.

    Returns:
        dict: Diccionario con las medianas de pH, Fósforo (P) y Potasio (K), o None si hay un error.
    """
    if not isinstance(resultados_df, pd.DataFrame):
        raise ValueError("El parámetro 'resultados_df' debe ser un DataFrame de pandas.")
    
    try:
        # Seleccionar solo las columnas de interés
        variables_interes = ["ph_agua_suelo_2_5_1_0", "f_sforo_p_bray_ii_mg_kg", "potasio_k_intercambiable_cmol_kg"]
        
        # Verificar que todas las columnas de interés están presentes en el DataFrame
        for variable in variables_interes:
            if variable not in resultados_df.columns:
                raise KeyError(f"Columna '{variable}' no encontrada en los datos.")
        
        # Convertir las columnas a numérico, forzando errores a NaN
        for variable in variables_interes:
            resultados_df[variable] = pd.to_numeric(resultados_df[variable].str.replace(',', '.'), errors='coerce')
        
        # Calcular la mediana de cada variable, ignorando NaN
        medianas = resultados_df[variables_interes].median(skipna=True)

        # Convertir a diccionario para su fácil uso
        medianas_dict = medianas.to_dict()

        return medianas_dict

    except KeyError as e:
        print(f"Error: No se encontró la columna esperada en los datos: {e}")
        return None
    except Exception as e:
        print(f"Ocurrió un error al calcular las medianas: {e}")
        return None
