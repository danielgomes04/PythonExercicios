from Exercicios import Exercicios

class Control:
    def __init__(self):
        self.exer = Exercicios()#conectando com a classe exercicios
        self.opcao = -1
        self.num1 = 0


    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def getNum1(self):
        return self.num1

    def setNum1(self, num1):
        self.num1 = num1

    def coletar(self):
        print("Escolha um número:")
        self.setNum1(self(input))


    def menu(self):
        print("\nEscolha um dos exercícios listados." +
                      "\nExercício 1. " +
                      "\nExercício 2. " +
                      "\nExercicio 3. " +
                      "\nExercicio 4. " +
                      "\nExercicio 5. " +
                      "\nExercicio 6  " +
                      "\nExercicio 7  " +
                      "\nExercicio 8  " +
                      "\nExercicio 9  " )
        self.setOpcao(int(input()))

    def operacao(self):
        while (self.getOpcao() != 0):
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado.")
            elif self.getOpcao() == 1:
                print(self.exer.exercicio1())
            elif self.getOpcao() == 2:
                self.coletar()
                print("Digite um número: {}".format(self.exer.exercicio2()))


