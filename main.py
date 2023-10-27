from microbit import *

# Configuración de los pines del sensor TCS3200
S0 = pin0
S1 = pin1
S2 = pin2
S3 = pin3
OUT = pin4

# Configuración de la frecuencia de muestreo del sensor
S0.write_digital(0)
S1.write_digital(1)

def detectar_color():
    # Configuración del sensor para detectar el color
    S2.write_digital(0)
    S3.write_digital(0)
    
    # Esperar a que el sensor se estabilice
    sleep(200)
    
    # Leer el valor del pin de salida del sensor
    r = OUT.read_digital()
    
    # Configuración del sensor para contar el color
    S2.write_digital(1)
    S3.write_digital(1)
    
    # Esperar a que el sensor se estabilice
    sleep(200)
    
    # Leer el valor del pin de salida del sensor
    b = OUT.read_digital()
    
    # Devolver el color detectado
    if r == 0 and b == 1:
        return "Rojo"
    elif r == 1 and b == 0:
        return "Azul"
    else:
        return "Desconocido"

while True:
    color = detectar_color()
    display.scroll("Color detectado: " + color)
    sleep(1000)
