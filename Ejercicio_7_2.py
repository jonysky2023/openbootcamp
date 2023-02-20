import time

while True:
    tactual = time.localtime()
    trestante = (19 - tactual.tm_hour) * 3600 + (60 - tactual.tm_min) * 60 - tactual.tm_sec

    if trestante <= 0:
        print("¡Ya es la hora!")
        break

    print(f"Tiempo restante: {trestante // 3600:02d}:{trestante % 3600 // 60:02d}:{trestante % 60:02d}")

    time.sleep(3)