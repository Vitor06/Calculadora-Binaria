import math

NUMERO_DE_BITS =16 #Quantidade de bits dos números

class Calculadora:
 
           
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
                #binario.insert(0,resto)
                binario =  str(resto) + binario 
            binario = str(qociente) + binario 

        elif(num==1):binario = binario + "1"
        elif (num==0):binario = binario + "0"
        return  binario

    def getNumBinario(self,num):
        numbin = self.ConverterNumeroParaBinario(abs(num))
        return numbin

    def transformaECompletaComZero(self,num):

        numbin = self.ConverterNumeroParaBinario(abs(num))
        
        for bit in range(NUMERO_DE_BITS-len(numbin)):
            numbin = "0" + numbin
  
        return numbin

    def soma(self,num1,num2):
        # 0 + 0 = 0
        # 0 + 1 = 1
        # 1 +0  = 1
        # 1 + 1 = 1 e vai 1
        bitesq = ""
        somaRes = ""
        vaiUm = ""
        #Se não for uma string
        if(type(num1)!=str and type(num2)!=str):
            if(num1==0):
                return self.transformaECompletaComZero(num2)
            elif(num2==0):
                return self.transformaECompletaComZero(num1)

            elif((num1<0 and num2>0)  or (num2< 0 and num1>0)):
                if(abs(num1) >= abs(num2)):
                    
                    if(num1<0):
                        bitesq  ="1"

                    return self.sub(abs(num1),abs(num2),bitesq)
 
                elif(abs(num2)>abs(num1)):

                    if(num2<0):   
                        bitesq  ="1"
            
                    return self.sub(abs(num2),abs(num1),bitesq)

            elif((num1<0 and num2<0) or (num1>0 and num2>0)):
            
                if(num1<0 and num2<0):
                    bitesq = "1"
            numbin1= self.transformaECompletaComZero(num1)
            numbin2= self.transformaECompletaComZero(num2)
        
        #Se for uma string 
        elif(type(num1)==str and type(num2)==str):
 
            numbin1 = num1
            numbin2 = num2
    
        print(numbin1 + " + " + numbin2 )
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
            if( bit ==0 and vaiUm == "1"):
                    somaRes = "1"  + somaRes
                    print()
                    print("Overflow")
                    print()

        
            print("Passo " + str(len(numbin1)-bit) + ":" + somaRes)
        if(bitesq=="1"):
            somaRes  = somaRes.replace("0",bitesq,1)

        return somaRes

    def sub(self,num1,num2,bitesq):
        # 0 - 0 = 0
        # 0 - 1 = 1 e vai um
        # 1 -0  = 1
        # 1 - 1 = 0

        subRes = ""
        vemUm = ""
       
        if(type(num1)!=str and type(num2)!=str):
            numbin1= self.transformaECompletaComZero(num1)
            numbin2= self.transformaECompletaComZero(num2)
        else:
            numbin1 = num1
            numbin2 = num2
        
        print(numbin1 + " - " + numbin2 )
        print()
        for bit in range(len(numbin1)-1,-1,-1):
            if( vemUm!="1"):
                if((numbin1[bit]=="0" and numbin2[bit]=="0") ):
                        vemUm = "0"
                        subRes = "0" + subRes  

                elif(numbin1[bit]=="1" and numbin2[bit]=="1" ):
                        vemUm = "0"
                        subRes = "0" + subRes  

                elif(numbin1[bit]=="0" and numbin2[bit]=="1"):
                        vemUm = "1" 
                        subRes = "1" + subRes 
                elif(numbin1[bit]=="1" and numbin2[bit]=="0"):
                        vemUm = "0" 
                        subRes = "1" + subRes 

            elif(vemUm == "1"):
                    if((numbin1[bit]=="1" and numbin2[bit]=="0")  ):
                        vemUm = "0"
                        subRes = "0"  + subRes
                    elif((numbin1[bit]=="1" and numbin2[bit]=="1")or(numbin1[bit]=="0" and numbin2[bit]=="0")):
                        vemUm = "1"
                        subRes = "1"  + subRes
                    
                    elif(numbin1[bit]=="0" and numbin2[bit]=="1" ):
                            vemUm = "1"
                            subRes = "0" + subRes 

            if( bit ==0 and vemUm == "1"):
                print("Underflow")
                subRes = "1"  + subRes
            print("Passo " + str(len(numbin1)-bit) + ":" + subRes)
        if(bitesq=="1"):
            subRes  = subRes.replace("0",bitesq,1)

        return subRes

    def subtracao(self,num1,num2):
        

        result = self.soma(num1,-num2)
        return result

    def divisao(self,num1,num2):
        count = 0;
        if(num1==0):return self.transformaECompletaComZero(0)
        elif(num2==0):return "Divisao não possivel"
        #Verificando se o divisor é menor que o dividendo
        elif(abs(num2)>abs(num1)):
            if(num1<0):

                R =self.transformaECompletaComZero(num1).replace("0","1",1)
                Q = self.transformaECompletaComZero(0)

                return "Qociente:" + Q,"Resto:" + R
            else:

                R = self.transformaECompletaComZero(num1)
                Q = self.transformaECompletaComZero(0)

                return "Qociente:" + Q,"Resto:" + R
        else:
            print("0"+" - Subtração")
            result = self.sub(abs(num1),abs(num2),"0")
            print()
            num2str = self.transformaECompletaComZero(num2)
            count = count +1

            for i in range(1,math.trunc(abs(num1)/abs(num2))):
                print()
                print(str(i)+" - Subtração")

                result = self.sub(result,num2str,"0")
                count = count +1

            #Verificando se há números negativos
            if(num1<0 or num2<0):
                
                        if((num1<0 and num2>0)):

                            result = result.replace("0","1",1)
                            count =  self.transformaECompletaComZero(count).replace("0","1",1)
                    
                        elif(num1>0 and num2<0):
                            
                            count = self.transformaECompletaComZero(count).replace("0","1",1)

                        elif(num1<0 and num2<0):

                               result =result.replace("0","1",1)
                               count = self.transformaECompletaComZero(count)

            else:count = self.transformaECompletaComZero(count)
            print()
            print("Qociente:" + count)
            print("Resto:" +result)

            
    def multiplicacao(self,num1,num2):
        if(num1==0 or num2 ==0):return self.transformaECompletaComZero(0)
        else:
            cont = NUMERO_DE_BITS
            A = self.transformaECompletaComZero(0)
            C = "0"
            Q = self.transformaECompletaComZero(num1)
            M = self.transformaECompletaComZero(num2)

            print()
            print("---------------------Inicio---------------------")
            print()
            print("C: " + C)
            print("A: " + A)
            print("Q: " + Q)
            print("M: " + M)
            print()

            while(cont!=0):
                print("*****************Ciclo " + str(NUMERO_DE_BITS-cont)+"*****************")
                if(Q[-1]=="1"):
                    
                    print("C,A <-- A + M ")
                    print()
                    A = self.soma(A,M)
                    print()

                    print("C: " + C)
                    print("A: " + A)
                    print("Q: " + Q)
                    print("M: " + M)

                    #Se houver overflow
                    if(len(A)>NUMERO_DE_BITS):
                        C = "1"
                        A = A[1:]

                        print()
                        print("Overflow")
                        print("C: " + C)
                        print("A: " + A)
                        print("Q: " + Q)
                        print("M: " + M)

                #Deslocamento há direita
                print()
                print("Deslocamento à Direita")
                print()
                A = C + A 
                C="0"
                Q = A[-1]  + Q 
                A = A[0:len(A)-1]
                Q = Q[0:len(Q)-1]

                cont = cont-1
               
                print()
                print("C: " + C)
                print("A: " + A)
                print("Q: " + Q)
                print("M: " + M)
                print("------------------------------------")

    

    
        
def menu():
        print("Digite 1 para a Soma")
        print("Digite 2 para a Subtracao")
        print("Digite 3 para a Divisao")
        print("Digite 4 para a Multiplicacao")
        print("Digite 5 para a Sair")

def main():

    calculadora = Calculadora()
    listopcao = ["1","2","3","4","5"]
  
    while(True):
        
        print("------------------------")
        menu()

        print("------------------------")
        opcao = input("Digite a opcao :")
        print("----------------------------")

        if (opcao=="5") :   break  
        
        elif(opcao in listopcao): 
            num1 = int(input("Digite o  numero 1:"))
            num2 = int(input("Digite o  numero 2:"))
            print()
            print("Numero 1 :" + calculadora.getNumBinario(num1))
            print( "Numero 2 :" + calculadora.getNumBinario(num2))
            print("----------------------------")

            if(opcao=="1"):print("Resultado:"+ calculadora.soma(num1,num2))
            elif(opcao=="2"):print("Resultado:"+calculadora.subtracao(num1,num2))
            elif(opcao=="3"):print(calculadora.divisao(num1,num2))
            elif(opcao=="4"):calculadora.multiplicacao(num1,num2)
        else:
            print("Opcao invalida")



main()

        