class Exercicios:
    def __init__(self):
        pass


    def exercicio1(self):
        self.a = 10
        self.b = 20
        self.c = self.a
        self.a = self.b
        self.b = self.c
        return "A: {} \nB: {}".format(self.a, self.b)

    def exercicio2(self, num):
        print("Informe um número: ")
        num = int(input())
        print ("O antecessor é: ", num - 1)

    def exercicio3(self, base, altura):
        print("informe uma base para o triangulo:")
        base = int(input())
        print("informe a altura:")
        altura = int(input())
        print("a area é: ", base * altura)

    def exercicio4(self, anos, mes, dia, total):
        print("informe quantos anos de vida voce tem:")
        anos = int(input())
        print("informe o mes atual: ")
        mes = int(input())
        print("informe o dia atual: ")
        dia = int(input())
        total = anos * 365  + mes * 30 + dia
        print("voce tem: ", total, "de vida")

    def exercicio5(self, quantEleitor, brancos, nulos, validos):
        print("Informe a quantidade de eleitores: ")
        quantEleitor = int(input())
        print("Quantidade de votos brancos: ")
        brancos = int(input())
        print("Quantidade de votos nulos: ")
        nulos = int(input())
        print("Quantidade de votos válidos: ")
        validos = int(input())
        print("A porcentagem de votos brancos é: ", quantEleitor * brancos / 100)
        print("A quantidade de votos nulos é: ",  quantEleitor * nulos / 100)
        print("A quantidade de votos válidos é: ",  quantEleitor * validos / 100)

    def exercicio6(self, salario, reajuste):
        print("Informe seu salário: ")
        salario = float(input())
        print("Digite o percentual de reajuste: ")
        reajuste = float(input())
        print("O novo salario é: ", reajuste / 100 * salario + salario)

    def exercicio7(self, carro, distribuidor, imposto, total):
        print("Informe o preço do carro: ")
        carro = float(input())
        distribuidor = 28 / 100
        imposto = 45 / 100
        total = (distribuidor + imposto) * carro + carro
        print("O custo final ao consumidor é: ", total)

    def exercicio8(self, nota1, nota2, nota3):
        print("Informe a primeira nota: ")
        nota1 = int(input())
        print("Informe a segunda nota: ")
        nota2 = int(input())
        print("Informe a terceira nota: ")
        nota3 = int(input())
        print("A nota final é: ", (nota1 + nota2 + nota3) / 3)

    def exercicio9(self, macas, macasMa, macasMe):
        print("informe a quantidade de maças compradas: ")
        macas = int(input())
        if macas >= 12:
            macasMa = 1 * macas
        elif macas < 12:
            macasMe = 1.30 * macas
        print("O total é: ", macasMa or macasMe)










