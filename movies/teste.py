Aponte quais os resultados das saídas de 1 a 5 (comentadas) e justifique resumidamente o porquê de sua resposta:

class FazAlgo():
    def __init__(self, parametroA: int = 5, parametroB: int = 3):
        self.parametroA = parametroA
        self.parametroB = parametroB
        self.__parametroC = parametroA * parametroB

    def printResult(self):
        print("O resultado é: ", self.__parametroC)

if __name__ == "__main__":
    Objeto1 = FazAlgo(4,2)
    Objeto1.printResult()             #Saída numero 1

    Objeto1.__parametroC = 53
    Objeto1.printResult()             #Saída numero 2

    Objeto2 = FazAlgo(parametroB = 7)
    c = Objeto2.printResult()         #Saída numero 3
    print(c)                          #Saída numero 4

    Objeto2.parametroA = 10
    Objeto2.printResult()             #Saída numero 5