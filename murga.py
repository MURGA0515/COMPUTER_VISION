import sys

print("\n=========================================")
print("      🚀 ¡ENTORNO CONFIGURADO CON ÉXITO!  ")
print("=========================================\n")

version_actual = sys.version.split()[0]
print(f"🔹 Python activo en el entorno: {version_actual}")

numero_base = 10
resultado = (numero_base * 5) + 50

if resultado == 100:
    print("✅ Prueba matemática: PASADA (10 * 5 + 50 = 100)")

print("\n=========================================")