# numero = int(input("indique um numero de 0 a 20: "))

# while numero <=0 or numero>20 :
#     print("ERRO indique um numero entre 0 a 20: \n")
#     numero = int(input("indique um numero de 0 a 20: "))

# numero= int(input("numero de 0 a 20"))
 
# while numero <=0 or numero >20:
#     print("erro indique um numero de 0 a 20" )
#     numero=(int(input("indique um numero de 0 a 20")))

# tabuada =int(input("imprime a tabuada dos: "))
# numero= 1
# while numero <11:
#     print("{:n} * {:n} = {:n}".format(tabuada,numero,tabuada*numero))
#     numero+=1

#import random

# palpite=(int(input("Guess a number: ")))
# numeroGerado=random.randint (0,10)
# tentativas=(1)
# while palpite != numeroGerado:
#     print("errou tente novamente: ")
#     palpite=(int(input("Guess a number: ")))
#     tentativas+=1
#     print("fez ",tentativas ,"tentativas")  
# print(f"acertou em {tentativas} tentativas")



# numeroTabuada = int(input("indique o nr da tabuada: "))
# numero=0
# while numeroTabuada < 11:
#     numero+=1
#     if numero == 6:
#         continue
#     print(numeroTabuada, "*" , numero, "=" , numeroTabuada*numero)
#     if numero == 10:
#         break
import math
maior= -math.inf

soma=0
for i in range(10):
    numero=(int(input("indique um numero ate 20: ")))
    soma+= numero
    if numero > maior:
        maior= numero

media= (soma/10)
print("A media é : ",media)
print("O maior é : ", maior)

    


 




          

