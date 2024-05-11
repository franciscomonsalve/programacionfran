#¿Cómo saber si un año es bisiesto? 
# Todos los años bisiestos son divisibles entre 4.
# Aquellos años que son divisibles entre 4,
# pero no entre 100, son bisiestos.
# Los años que son divisibles entre 100, pero no entre 400, no son bisiestos

año =int(input("Ingresar Año "))
if  año % 4 == 0  and  año % 100 != 0 or  año % 400 == 0  :
  print("Este año si es bisiesto")
  
else :
  print("Este año no es bisiesto")
 