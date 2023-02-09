def okbisiesto(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

fecha = int(input('Introduce un año:'))
if okbisiesto(fecha):
    print('Este año es bisiesto')
else:
    print('Este año NO es bisiesto')
