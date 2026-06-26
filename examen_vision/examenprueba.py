import sys
import time

def inicializar_sistema():
    print("\n==================================================")
    print("      📸 SISTEMA DE VISIÓN ARTIFICIAL ACTIVO      ")
    print("==================================================\n")
    time.sleep(1)
    
    # Simulación de carga de una matriz de píxeles (Imagen gris de 3x3)
    imagen_simulada = [
        [150, 200, 50],
        [90,  255, 15],
        [0,   180, 220]
    ]
    
    print("🔄 Cargando matriz de entrada (Píxeles)...")
    for fila in imagen_simulada:
        print(f"   {fila}")
    time.sleep(1)
    
    # Contar píxeles brillantes (Simulación de umbralizado)
    umbrales_altos = 0
    for fila in imagen_simulada:
        for pixel in fila:
            if pixel > 100:
                umbrales_altos += 1
                
    print(f"\n✨ Análisis terminado:")
    print(f"🔹 Píxeles con alta intensidad (>100): {umbrales_altos}/9")
    print(f"🔹 Python Ejecutable: {sys.executable}")
    print("\n==================================================")
    print("         ✅ EXAMEN LISTO PARA SUBIR A GIT        ")
    print("==================================================")

if __name__ == "__main__":
    inicializar_sistema()