from Exercicios import Exercicios

class Control:
    def __init__(self):
        self.exer = Exercicios()#conectando com a classe exercicios
        self.opcao = -1
        self.num1 = 0
        self.base = 0
        self.altura = 0
        self.dia = 0
        self.mes = 0
        self.anos = 0
        self.total = 0
        self.quantEleitor = 0
        self.brancos = 0
        self.nulos = 0
        self.validos = 0
        self.salario = 0
        self.reajuste = 0


    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def getNum1(self):
        return self.num1

    def setNum1(self, num1):
        self.num = num1


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
        while(self.getOpcao() != 0):
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado.")
                break
            elif self.getOpcao() == 1:
                print(self.exer.exercicio1())
            elif self.getOpcao() == 2:
                print(self.exer.exercicio2(self.getNum1()))
            elif self.getOpcao() == 3:
                print(self.exer.exercicio3(self.base, self.altura))
            elif self.getOpcao() == 4:
                print(self.exer.exercicio4(self.anos, self.mes, self.dia, self.total))
            elif self.getOpcao() == 5:
                print(self.exer.exercicio5(self.quantEleitor, self.brancos, self.nulos, self.validos))
            elif self.getOpcao() == 6:
                print(self.exer.exercicio6(self.salario, self.reajuste))
            elif self.getOpcao() == 7:
                print(self.exer.exercicio7(self.))


