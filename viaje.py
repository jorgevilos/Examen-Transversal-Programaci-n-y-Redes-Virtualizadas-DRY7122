from geopy.distance import geodesic

# Coordenadas de algunas ciudades de ejemplo
ciudades = {
    "Santiago de Chile": (-33.4489, -70.6693),
    "Lima": (-12.0464, -77.0428)
}

medios_transporte = {
    "avión": 900,  # Velocidad promedio en km/h
    "auto": 100,   # Velocidad promedio en km/h
    "tren": 120    # Velocidad promedio en km/h
}

def calcular_distancia(origen, destino):
    return geodesic(ciudades[origen], ciudades[destino]).kilometers

def convertir_millas(kilometros):
    return kilometros * 0.621371

def duracion_viaje(distancia, velocidad):
    return distancia / velocidad

def mostrar_narrativa(origen, destino, distancia, duracion, transporte):
    print(f"\nNarrativa del viaje de {origen} a {destino}:")
    print(f"La distancia entre {origen} y {destino} es de {distancia:.2f} kilómetros o {convertir_millas(distancia):.2f} millas.")
    print(f"Viajando en {transporte}, la duración estimada del viaje es de {duracion:.2f} horas.\n")

def main():
    while True:
        print("\n---- Planificador de Viajes ----")
        ciudad_origen = input("Ciudad de Origen (o presiona 'e' para salir): ").strip()
        if ciudad_origen.lower() == 'e':
            break
        ciudad_destino = input("Ciudad de Destino (o presiona 'e' para salir): ").strip()
        if ciudad_destino.lower() == 'e':
            break
        
        if ciudad_origen not in ciudades or ciudad_destino not in ciudades:
            print("Una de las ciudades ingresadas no está en la lista. Inténtalo de nuevo.")
            continue
        
        print("Selecciona el medio de transporte: avión, auto, tren")
        transporte = input("Medio de transporte: ").strip().lower()
        if transporte not in medios_transporte:
            print("Medio de transporte no válido. Inténtalo de nuevo.")
            continue
        
        distancia = calcular_distancia(ciudad_origen, ciudad_destino)
        duracion = duracion_viaje(distancia, medios_transporte[transporte])
        
        mostrar_narrativa(ciudad_origen, ciudad_destino, distancia, duracion, transporte)

if __name__ == "__main__":
    main()
