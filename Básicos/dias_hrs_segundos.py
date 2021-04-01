inicial = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dias = int(inicial/86400)
aux = int(inicial % 86400)

horas = int(aux/3600)
aux2= int(aux % 3600)

minutos = int(aux2/60)

segundos = int(aux2 % 60)

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
