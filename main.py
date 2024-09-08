from UI.UI_modulo import obtener_datos_usuario
from API.API_modulo import obtener_datos_suelos, calcular_mediana_variables_edaficas

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
            print(f"pH: {medianas.get('ph_agua_suelo_2_5_1_0', 'No disponible')}")
            print(f"Fósforo: {medianas.get('f_sforo_p_bray_ii_mg_kg', 'No disponible')}")
            print(f"Potasio: {medianas.get('potasio_k_intercambiable_cmol_kg', 'No disponible')}")
        else:
            print("No se pudieron calcular las medianas.")
    else:
        print("No se obtuvieron datos para calcular las medianas.")

    print("Gracias por utilizar la aplicación. ¡Que tengas un excelente día!")

if __name__ == "__main__":
    main()
