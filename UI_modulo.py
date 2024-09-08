def obtener_datos_usuario():
    """
    Returns:
        tuple: (departamento, municipio, cultivo, limite)
    """
    NUMERO_MAXIMO_REGISTROS = 500  
    print("¡Bienvenido a la aplicación de consulta de análisis de suelos!")
    
    Departamento = input("Por favor, ingrese el nombre del departamento: ").strip()
    while not Departamento:
        print("El departamento no puede estar vacío. Por favor, ingrese un nombre válido.")
        Departamento = input("Por favor, ingrese el nombre del departamento: ").strip()
    
    Municipio = input("Por favor, ingrese el nombre del municipio: ").strip()
    while not Municipio:
        print("El municipio no puede estar vacío. Por favor, ingrese un nombre válido.")
        Municipio = input("Por favor, ingrese el nombre del municipio: ").strip()
    
    Cultivo = input("Por favor, ingrese el nombre del cultivo: ").strip()
    while not Cultivo:
        print("El cultivo no puede estar vacío. Por favor, ingrese un nombre válido.")
        Cultivo = input("Por favor, ingrese el nombre del cultivo: ").strip()
    
    while True:
        try:
            limite = int(input(f"Ingrese el número de registros a consultar (máximo {NUMERO_MAXIMO_REGISTROS}): "))
            if limite <= 0:
                raise ValueError("El número de registros debe ser mayor a cero.")
            if limite > NUMERO_MAXIMO_REGISTROS:
                print(f"El número máximo de registros permitido es {NUMERO_MAXIMO_REGISTROS}. Por favor, ingrese un número menor o igual a {NUMERO_MAXIMO_REGISTROS}.")
            else:
                break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, intente nuevamente.")
    
    print("Muchas Gracias por proporcionar la información. Estamos procesando su consulta...")
    
    return Departamento, Municipio, Cultivo, limite
