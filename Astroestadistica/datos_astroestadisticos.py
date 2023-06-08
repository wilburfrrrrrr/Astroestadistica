import matplotlib.pyplot as plt
from collections import Counter 

def calcular_probabilidad(planeta):
    with open('planetas.txt', 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if planeta in linea:
                indice_inicio = linea.index(':') + 1
                indice_fin = linea.index('.')
                datos_planeta = linea[indice_inicio:indice_fin]
                contador = datos_planeta.count('+')
                probabilidad = (contador / 4) * 100
                
                return probabilidad
        
        # Si el planeta no se encuentra en el archivo
        return None

def calcular_moda_probabilidad():
    lista_probabilidades = []
    
    with open('planetas.txt', 'r') as archivo:
        lineas = archivo.readlines()
        
        for linea in lineas:
            if '+' in linea:
                indice_inicio = linea.index(':') + 1
                indice_fin = linea.index('.')
                datos_planeta = linea[indice_inicio:indice_fin]
                contador = datos_planeta.count('+')
                probabilidad = (contador / 4) * 100
                
                lista_probabilidades.append(probabilidad)
    
    if lista_probabilidades:
        conteo = Counter(lista_probabilidades)
        moda_probabilidad = conteo.most_common(1)[0][0]
        return moda_probabilidad
    
    return None

def generar_grafica_barras(planetas):
    probabilidades = {}
    for planeta in planetas:
        probabilidad = calcular_probabilidad(planeta)
        if probabilidad is not None:
            probabilidades[planeta] = probabilidad
    
    planetas = list(probabilidades.keys())
    valores = list(probabilidades.values())

    # Configurar la figura y los ejes de la gráfica
    fig, ax = plt.subplots()

    # Crear la gráfica de barras
    ax.bar(planetas, valores)

    # Personalizar la gráfica
    ax.set_xlabel('Planetas')
    ax.set_ylabel('Probabilidad (%)')
    ax.set_title('Probabilidad de Habitabilidad de Planetas')

    # Mostrar la gráfica
    plt.show()

def calcular_media_probabilidad():
    total_probabilidad = 0
    total_planetas = 0
    
    with open('planetas.txt', 'r') as archivo:
        lineas = archivo.readlines()
        
        for linea in lineas:
            if '+' in linea:
                indice_inicio = linea.index(':') + 1
                indice_fin = linea.index('.')
                datos_planeta = linea[indice_inicio:indice_fin]
                contador = datos_planeta.count('+')
                probabilidad = (contador / 4) * 100
                
                total_probabilidad += probabilidad
                total_planetas += 1
    
    if total_planetas > 0:
        media_probabilidad = total_probabilidad / total_planetas
        return media_probabilidad
    
    return None


def mostrar_menu():
	print("=== MENÚ ===")
	print("1. Calcular probabilidad de habitabilidad de un planeta")
	print("2. Generar gráficas de barras")
	print("3. Calcular promedio de vida en todos los planetas")
	print("4. Calcular moda de probabilidad de vida en todos los planetas")
	print("0. Salir")

def main():
		# Obtener la lista de nombres de planetas del archivo
			with open('planetas.txt', 'r') as archivo:
				lineas = archivo.readlines()
				planetas = [linea[linea.index('-')+1:linea.index(':')].strip() for linea in lineas]
			
			while True:
				mostrar_menu()
				opcion = input("Ingrese una opción: ")
				print()
				
				if opcion == '1':
					# Mostrar la lista de planetas numerados
					print("Lista de planetas:")
					for i, planeta in enumerate(planetas):
						print(f"{i+1}. {planeta}")
					print()
					
					# Solicitar al usuario que elija un número de planeta
					num_planeta = int(input("Ingrese el número del planeta deseado: "))
					print()
					
					if num_planeta >= 1 and num_planeta <= len(planetas):
						planeta_elegido = planetas[num_planeta - 1]
						
						# Calcular la probabilidad del planeta elegido
						probabilidad = calcular_probabilidad(planeta_elegido)
						
						if probabilidad is not None:
							print(f"La probabilidad de habitabilidad de {planeta_elegido} es: {probabilidad}%")
						else:
							print("El planeta no se encuentra en la lista.")
					else:
						print("Número de planeta inválido. Intente nuevamente.")
					
					print()
				
				elif opcion == '2':
					# Mostrar la lista de planetas numerados
					print("Lista de planetas:")
					for i, planeta in enumerate(planetas):
						print(f"{i+1}. {planeta}")
					print()
					
					# Solicitar al usuario que elija cinco números de planetas
					planetas_grafica = []
					for i in range(5):
						num_planeta = int(input(f"Ingrese el número del planeta {i+1}: "))
						if num_planeta >= 1 and num_planeta <= len(planetas):
							planeta_elegido = planetas[num_planeta - 1]
							planetas_grafica.append(planeta_elegido)
						else:
							print("Número de planeta inválido. Se omitirá.")
					print()
					
					# Calcular las probabilidades de los planetas seleccionados
					probabilidades = {}
					for planeta in planetas_grafica:
						probabilidad = calcular_probabilidad(planeta)
						if probabilidad is not None:
							probabilidades[planeta] = probabilidad
					
					# Generar la gráfica de barras
					generar_grafica_barras(probabilidades)
				
				elif opcion == '3':
					media = calcular_media_probabilidad()
					if media is not None:
						print(f"La media de probabilidad de vida de los planetas es: {media}%")
					else:
						print("No se encontraron planetas en el archivo.")

				elif opcion == '4':
					moda = calcular_moda_probabilidad()
					if moda is not None:
						print(f"La mayoria de los planetas tiene un porcentaje de vida de: {moda}%")
					else:
						print("No se encontraron planetas en el archivo.")

				elif opcion == '0':
					print("¡Hasta luego!")
					break
				
				else:
					print("Opción inválida. Intente nuevamente.")
				
				print()

if __name__ == "__main__":
    main()
