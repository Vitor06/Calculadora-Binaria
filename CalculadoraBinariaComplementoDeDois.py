
import math

NUMERO_DE_BITS =16#Quantidade de bits dos números
class Calculadora:
    def __init__(self,operador):
        self.operador =operador
           
    def ConverterNumeroParaBinario(self,num):
        binario = ""
        if(num!=1 and num!=0):
        
            num =abs(num)

            qociente = num//2
            resto = num%2
            binario =  str(resto) + binario 

            while(qociente!=1):
        
                resto = qociente%2
                qociente = qociente//2
                binario =  str(resto) + binario 
            binario = str(qociente) + binario 

        elif(num==1):binario = binario + "1"
        elif (num==0):binario = binario + "0"
        return  binario

 

    def transformaECompletaComZero(self,num):
        numBits = NUMERO_DE_BITS
        numbin = self.ConverterNumeroParaBinario(abs(num))
        for bit in range(numBits-len(numbin)):
            numbin = "0" + numbin
  
        return numbin

   
    def soma(self,num1,num2):
        # 0 + 0 = 0
        # 0 + 1 = 1
        # 1 +0  = 1
        # 1 + 1 = 1 e vai 1
        somaRes = ""
        vaiUm = ""

        numbin1 = num1
        numbin2 = num2

    
        print("Soma")
        print(numbin1 + " + " + numbin2)
        print()
        for bit in range(len(numbin1)-1,-1,-1):
            if( vaiUm!="1"):
                if((numbin1[bit]=="1" and numbin2[bit]=="0") or (numbin1[bit]=="0" and numbin2[bit]=="1")):
                        vaiUm = "0"
                        somaRes = "1" + somaRes  

                elif(numbin1[bit]=="0" and numbin2[bit]=="0" ):
                            vaiUm = "0"
                            somaRes = "0" + somaRes  

                elif(numbin1[bit]=="1" and numbin2[bit]=="1"):
                            vaiUm = "1" 
                            somaRes = "0" + somaRes 

            elif(vaiUm == "1"):
                if((numbin1[bit]=="1" and numbin2[bit]=="1")  ):
                        vaiUm = "1"
                        somaRes = "1"  + somaRes
                elif((numbin1[bit]=="1" and numbin2[bit]=="0")or (numbin1[bit]=="0" and numbin2[bit]=="1")):
                        vaiUm = "1"
                        somaRes = "0"  + somaRes

                elif(numbin1[bit]=="0" and numbin2[bit]=="0" ):
                            vaiUm = "0"
                            somaRes = "1" + somaRes 
            
         
            print("Passo " + str(len(numbin1)-bit) + ":" + somaRes)
        


        return somaRes

    

    def divisao(self,num1,num2):
        numBits =NUMERO_DE_BITS
        if(num1==0):return self.transformaECompletaComZero(0)
        elif(num2==0):return "Divisao não possivel"
        elif(abs(num2)>abs(num1)):
            if(num1<0):
                R = self.complemento(self.transformaECompletaComZero(num1))
                Q = self.transformaECompletaComZero(0)
                return "Qociente:" + Q,"Resto:" + R
            else:
                R = self.transformaECompletaComZero(num1)
                Q = self.transformaECompletaComZero(0)
                return "Qociente:" + Q,"Resto:" + R

    
        #Inicialização de Variáveis
        Q = self.transformaECompletaComZero(abs(num1))
        M = self.transformaECompletaComZero(abs(num2))
        A = self.transformaECompletaComZero(0)

        print()
        print("M_Linha")
        M_linha = self.complemento(M)
        
        print("------------------Inicio-------------------")
        print()
        print("A: " + A)
        print("Q: " + Q)
        print("M: " + M)
        print("M_Linha: " + M_linha)

        print()
        while(numBits!=0):
            #deslocamento
            print("****Ciclo**** " + str(NUMERO_DE_BITS-numBits)+":")
            print()
            print("Deslocamento a esquerda A,Q")
            Q =   Q + "0" 
            A =  A + Q[0]
            Q = Q[1:]
            A = A[1:]

            print("A: " + A)
            print("Q: "+ Q)
            print("M: " + M)
            print("M_Linha: " + M_linha)

            print()
            #A=A-M
            print("A = A + M_Linha")

            A = self.soma(A,M_linha)
            print()
            print("A: " + A)
            print("Q: " + Q)
            print("M: " + M)
            print("M_Linha: " + M_linha)


            #Verificando Q_0
            if(A[0] == "1"):
                print()
                print("A < 0")
                print("Q_0 = 0")
                print("A = A + M")
                #Q_0 = 0
                Q = Q[0:len(Q)-1]+ "0"
                A = self.soma(A,M)
                print()

                print("A: " + A)
                print("Q: " + Q)
                print("M: " + M)
                print("M_Linha: " + M_linha)
                
            elif(A[0] == "0"):
                #Q_0 = 1
                Q = Q[0:len(Q)-1]+ "1"
                print()
                print("A > 0")
                print("Q_0 = 1")
                print("A: " + A)
                print("Q: " + Q)
                print("M: " + M)
                print("M_Linha: " + M_linha)
           
            numBits = numBits-1
            print("------------------------------------------")

        #Tratando Negativos                
        if(num1<0 or num2<0):
    
            print()
            print("Complementando quem é negativo")
            print()
            if((num1<0 and num2>0)):

                A = self.complemento(A)
                Q = self.complemento(Q)
        
            elif(num1>0 and num2<0):
                
                Q = self.complemento(Q)
        
    

            elif(num1<0 and num2<0):
                A = self.complemento(A)
        
        print()
        print("Resultado final:")
        print()
        print("A: " + A)
        print("Q: " + Q)
        print("M: " + M)
        print("M_Linha: " + M_linha)

        
        
            
    def multiplicacao(self,num1,num2):
        numBits = NUMERO_DE_BITS
        if(num1==0 or num2 ==0):return self.transformaECompletaComZero(0)

        #Inicializando as vatiáveis
        A = self.transformaECompletaComZero(0)
        Q = self.transformaECompletaComZero(abs(num2))
        Q_linha = "0"
        M = self.transformaECompletaComZero(abs(num1))
        

        #Tratando Sinal
        if(num1<0 or num2<0):
          
            if((num1<0 and num2>0) ):
                M = self.complemento(M)

            elif((num1>0 and num2<0)):
                Q = self.complemento(Q)

            elif(num1<0 and num2<0):
                M = self.complemento(M)
                Q = self.complemento(Q)
         
              

        M_linha = self.complemento(M)

        print()
        print("------------------Inicio-------------------")

        print("A: " + A)
        print("Q: " + Q)
        print("Q_linha: " + Q_linha)
        print("M: " + M)
        print("M_linha: " + M_linha)
   

        print()

        while(numBits!=0):
            print("Ciclo " + str(NUMERO_DE_BITS-numBits)+":")
            print()

            if(Q[-1]=="1" and Q_linha=="0"):
                print()
                print("Q_0 = 1 e Q_-1 = 0 ")
                print("A = A + M_Linha")
                A = self.soma(A,M_linha)

                print()
                
                print("A: " + A)
                print("Q: " + Q)
                print("Q_linha: " + Q_linha)
                print("M: " + M)
                print("M_linha: " + M_linha)

   

            elif(Q[-1]=="0" and Q_linha=="1"):
                print("Q_0 = 0 e Q_-1 = 1")

                print()
                print("A = A + M")
                A = self.soma(A,M)
                print()

                print("A: " + A)
                print("Q: " + Q)
                print("Q_linha: " + Q_linha)
                print("M: " + M)
                print("M_linha: " + M_linha)

                
            print()

            #Deslocamento atitimético a direita
            print("Deslocamento aritimético á direita A ,Q, Q_linha")
            print()

            A = A[0] + A
            Q = A[-1]  + Q 
            Q_linha = Q[-1]
          
            A = A[0:len(A)-1]
            Q = Q[0:len(Q)-1]

            print("A: " + A)
            print("Q: " + Q)
            print("Q_linha: " + Q_linha)
            print("M: " + M)
            print("M_linha: " + M_linha)



            numBits = numBits-1
            print("----------------------------------")

    def complemento(self,numBin):
        print("--------------------")
        print("Primeiro Passo : Invertendo o "+ str(numBin))
        print("--------------------")
        numbinResult= ""
        if(numBin ==self.transformaECompletaComZero(0)):return self.transformaECompletaComZero(0)


        for bit in range(len(numBin)-1,-1,-1):
            if(numBin[bit]=="1"):
               numbinResult  = "0" + numbinResult 
            else:
                numbinResult  = "1" + numbinResult 
           
            print(numbinResult)
        print()
        print("Segundo Passo:")
        numbinResult =self.soma(numbinResult,self.transformaECompletaComZero(1))
       

        print("Resultado : " + numbinResult)
       
        return numbinResult   


def menu():
        
        print("Digite 1 para a Multiplicacao")
        print("Digite 2 para a Divisao")
        print("Digite 3 para a Sair")

def main():
    calculadora = Calculadora("multi")
    listopcao = ["1","2","3"]
    while(True):
      
        print("------------------------")
        menu()

        print("------------------------")
        opcao = input("Digite a opcao :")
        print("----------------------------")

        if (opcao=="3") :   break  
        elif(opcao in listopcao):  

            num1 = int(input("Digite o  numero 1:"))
            num2 = int(input("Digite o  numero 2:"))
            print()
            print(str(abs(num1))+":" + calculadora.transformaECompletaComZero(num1))
            print(str(abs(num2)) +":" + calculadora.transformaECompletaComZero(num2))

            print()
  
            print("----------------------------")

            if(opcao=="1"):
                print("MULTIPLICAÇÃO")
                print(calculadora.multiplicacao(num1,num2))
            elif(opcao=="2"):
                print("DIVISÃO")
                print(calculadora.divisao(num1,num2))
        else:
            print("Oção inválida")




main()

        