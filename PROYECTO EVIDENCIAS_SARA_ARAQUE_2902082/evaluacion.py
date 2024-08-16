class Vivienda:
    def __init__(self, 
                 nombre, 
                 documento_identidad, 
                 correo_electronico, 
                 numero_celular):
        self.__nombre = nombre
        self.__documento_identidad = documento_identidad
        self.__correo_electronico = correo_electronico
        self.__numero_celular = numero_celular

    def mostrar_informacion(self):
        return (f"Name: {self.__nombre}\n"
                f"identity document: {self.__documento_identidad}\n"
                f"Email: {self.__correo_electronico}\n"
                f"Phone number: {self.__numero_celular}")

    def venta(self):
        raise NotImplementedError("El método 'venta' debe ser implementado en las subclases")

class Casa(Vivienda):
    def __init__(self, 
                 nombre, 
                 documento_identidad, 
                 correo_electronico, 
                 numero_celular,
                 direccion, 
                 barrio, 
                 localidad, 
                 valor_casa):
        super().__init__(nombre, 
                         documento_identidad, 
                         correo_electronico, 
                         numero_celular)
        
        self.__direccion = direccion
        self.__barrio = barrio
        self.__localidad = localidad
        self.__valor_casa = self.__validar_valor_casa(valor_casa)
        self.__matricula = 0
        self.__impuesto_predial = 0
        self.__calcular_matricula_e_impuesto()

    def __validar_valor_casa(self, valor_casa):
        while True:
            try:
                valor_casa = float(valor_casa)
                if 300 <= valor_casa <= 600:
                    return valor_casa
                else:
                    valor_casa = input("The value of the house must be between 300 million and 600 million. Try again:")
            except ValueError:
                valor_casa = input("Invalid entry. Please enter a number:")

    def __calcular_matricula_e_impuesto(self):
        self.__matricula = self.__valor_casa * 0.05
        self.__impuesto_predial = self.__matricula * 0.02
        
    def mostrar_informacion(self):
        informacion_vivienda = super().mostrar_informacion()
        return (f"{informacion_vivienda}\n"
                f"address: {self.__direccion}\n"
                f"neighborhood: {self.__barrio}\n"
                f"Locality: {self.__localidad}\n"
                f"Home Price: {self.__valor_casa}\n"
                f"Tituiton: {self.__matricula}\n"
                f"Property tax: {self.__impuesto_predial}")

    def venta(self):
        total_a_pagar = self.__valor_casa + self.__matricula + self.__impuesto_predial
        return (f"Home price: {self.__valor_casa}\n"
                f"tuition: {self.__matricula}\n"
                f"property tax: {self.__impuesto_predial}\n"
                f"total to pay: {total_a_pagar}")

class Apartamento(Vivienda):
    def __init__(self, 
                 nombre, 
                 documento_identidad, 
                 correo_electronico, 
                 numero_celular,
                 direccion, 
                 barrio, 
                 localidad, 
                 numero_apartamento, 
                 bloque_o_interior, 
                 piso, 
                 valor_apartamento):
        super().__init__(nombre, 
                         documento_identidad, 
                         correo_electronico, 
                         numero_celular)
        
        self.__direccion = direccion
        self.__barrio = barrio
        self.__localidad = localidad
        self.__numero_apartamento = numero_apartamento
        self.__bloque_o_interior = bloque_o_interior
        self.__piso = piso
        self.__valor_apartamento = valor_apartamento
        self.__impuestos = 0
        self.__calcular_impuestos()

    def __calcular_impuestos(self):
        if self.__piso >= 1 and self.__piso <= 3:
            self.__impuestos = self.__valor_apartamento * 0.03
        elif self.__piso >= 4 and self.__piso <= 8:
            self.__impuestos = self.__valor_apartamento * 0.10
        elif self.__piso >= 9:
            self.__impuestos = self.__valor_apartamento * 0.20

    def mostrar_informacion(self):
        informacion_vivienda = super().mostrar_informacion()
        return (f"{informacion_vivienda}\n"
                f"Address: {self.__direccion}\n"
                f"Neighborhood: {self.__barrio}\n"
                f"Locality: {self.__localidad}\n"
                f"Apartment Number: {self.__numero_apartamento}\n"
                f"Block or Interior: {self.__bloque_o_interior}\n"
                f"Floor: {self.__piso}\n"
                f"Apartment Value: {self.__valor_apartamento}\n"
                f"Taxes: {self.__impuestos}")

    def venta(self):
        return (f"Apartment Value: {self.__valor_apartamento}\n"
                f"Taxes:{self.__impuestos}\n"
                f"Total to Pay: {self.__valor_apartamento + self.__impuestos}")

def capturar_informacion_vivienda():
    tipo = input("Enter if your type of housing is (1/2): ").strip().lower()
    
    nombre = input("Enter the buyer's name:").strip()
    documento_identidad = input("Enter the buyer's identity document:").strip()
    correo_electronico = input("Enter buyer's email: ").strip()
    numero_celular = input("Enter the buyer's cell phone number: ").strip()

    direccion = input("Enter the address: ").strip()
    barrio = input("Enter the neighborhood: ").strip()
    localidad = input("Enter the location:").strip()

    if tipo == "1":
        valor_casa = input("Enter the value of the house:").strip().replace(',', '')
        try:
            casa = Casa(nombre, 
                        documento_identidad, 
                        correo_electronico, 
                        numero_celular,
                        direccion, 
                        barrio, localidad, 
                        valor_casa)
            
            print("\nHouse information:")
            print(casa.mostrar_informacion())
            print("\nSale details:")
            print(casa.venta())
        except ValueError as e:
            print(f"Error: {e}")
            
    elif tipo == "2":
        numero_apartamento = input("Enter apartment number: ").strip()
        bloque_o_interior = input("Enter the block or interior:").strip()
        piso = int(input("Enter the apartment floor: ").strip())
        valor_apartamento = float(input("Enter the value of the apartment: ").strip().replace(',', ''))
        try:
            apartamento = Apartamento(nombre, 
                                      documento_identidad, 
                                      correo_electronico, 
                                      numero_celular,
                                      direccion, 
                                      barrio, 
                                      localidad, 
                                      numero_apartamento, 
                                      bloque_o_interior, 
                                      piso, 
                                      valor_apartamento)
            
            print("\nApartment information:")
            print(apartamento.mostrar_informacion())
            print("\nSale details:")
            print(apartamento.venta())
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Invalid housing type. It must be 'house' or 'apartment':")

def main():
    while True:
        capturar_informacion_vivienda()
        continuar = input("\n¿Do you want to enter another home? (y/n):").strip().lower()
        if continuar != 'y':
            break

if __name__ == "__main__":
    main()
