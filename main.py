from UI.UI_modulo import obtener_datos_usuario
from API.API_modulo import obtener_datos_suelos, calcular_mediana_variables_edaficas

def imprimir_tabla(medianas):
    """
    Imprime los resultados en formato de tabla en la consola.
    """
    # Imprimir encabezado de la tabla
    print("+------------------------------+---------------------+")
    print("| Variable                     | Mediana             |")
    print("+------------------------------+---------------------+")
    
    # Imprimir cada fila de la tabla
    for variable, descripcion in [
        ("ph_agua_suelo_2_5_1_0", "pH"),
        ("f_sforo_p_bray_ii_mg_kg", "Fósforo"),
        ("potasio_k_intercambiable_cmol_kg", "Potasio")
    ]:
        mediana = medianas.get(variable, 'No disponible')
        # Ajustar el ancho de las columnas para alineación
        print(f"| {descripcion:<28} | {str(mediana):>19} |")
    
    # Imprimir línea final de la tabla
    print("+------------------------------+---------------------+")

def main():
    # Obtener datos del usuario
    Departamento, Municipio, Cultivo, limite = obtener_datos_usuario()

    # Obtener datos de la API
    datos = obtener_datos_suelos(Departamento, Municipio, Cultivo, limite)
    
    if datos is not None:
        # Calcular medianas si se obtienen datos
        medianas = calcular_mediana_variables_edaficas(datos)
        
        if medianas is not None:
            print("Medianas de las variables edáficas:")
            imprimir_tabla(medianas)
        else:
            print("No se pudieron calcular las medianas.")
    else:
        print("No se obtuvieron datos para calcular las medianas.")

    print("Gracias por utilizar la aplicación. ¡Que tengas un excelente día!")

if __name__ == "__main__":
    main()
