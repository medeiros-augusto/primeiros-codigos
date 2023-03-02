#Recebendo os dados

altura = float(input("Informe sua altura em metros: "))
peso = float(input("Informe seu peso: "))

#Calculando o IMC

IMC = peso / (altura**2) 

#Condição para determinar classificação de peso

if IMC < 18.5:
  print("Você está abaixo do peso e seu é IMC:", IMC)
elif IMC >= 18.5 and IMC < 25:
  print("Você está com o peso normal e seu é IMC:", IMC)
elif IMC >= 25 and IMC < 30:
  print("Você está acima do peso e seu é IMC:", IMC)
else:
  print("Você está obeso e seu é IMC:", IMC)