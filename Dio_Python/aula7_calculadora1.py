class Calculadora:
    def __init__(self,num,num1):
        self.a = num
        self.b = num1
    def soma(self):
        return(self.a + self.b)

    def subtracao(self):
        return(self.a - self.b)

    def multiplicacao(self):
        return (self.a * self.b)

    def divisao(self):
        return(self.a / self.b)
if __name__ == '__main__':
    calculadora = Calculadora(10,2)
    print(calculadora.soma())  
    print(calculadora.subtracao()) 
    print(calculadora.multiplicacao())
    print(calculadora.divisao())

