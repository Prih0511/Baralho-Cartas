class Cartas:

#Um naipe (ouros, copas, espadas ou paus) e um valor (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, Q, J ,K). ok
    VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Q", "J" ,"K"] 
    NAIPES = ["ouros" , "copas" , "espadas" , "paus"]


    def __init__ (self, valor, naipe):
        self.valida_carta(valor, naipe)
        self.valor = valor
        self.naipe = naipe

#Um método de validação que verifique se o naipe e o valor da carta estão entre as opções permitidas. ok
    def valida_carta(self, valor, naipe):
        if valor not in self.VALORES:
            raise Exception(f"Valor invalido, tente outro: {valor}")
        if naipe not in self.NAIPES:
            raise Exception(f"Naipe invalido, tente outro: {naipe}")

#Um método que permita imprimir diretamente a identidade da carta (naipe + valor) ok
    def mostrar (self):
        print (f"{self.valor}  {self.naipe}")


    def __str__ (self):
        return f" Carta: {self.valor}  {self.naipe}"


    def mudando_valores (self, valor, outro):
    #A vale 1, Q vale 11, J vale 12 e o K , valor for maior. 13. ok
        if valor == "A":
            self.valor = "1"
        
        if outro.valor == "A":
            outro.valor = "1"

        if valor == "Q":
            self.valor = "11"
        
        if outro.valor == "Q":
            outro.valor = "11"
        
        if valor == "J":
            self.valor = "12"

        if outro.valor == "J":
            outro.valor = "12"

        if valor == "K":
            self.valor = "13"

        if outro.valor == "K":
            outro.valor = "13"

#Métodos de comparação (__gt__, __lt__, __eq__) entre cartas. Considere que: 
    def __gt__ (self, outro):
        self.mudando_valores(self.valor, outro )

        return self.valor > outro.valor
            
            
    def __lt__ (self, outro):
        self.mudando_valores(self.valor, outro )

        return self.valor < outro.valor


    def __eq__ (self, outro):
        self.mudando_valores(self.valor, outro )

        return self.valor == outro.valor
    
