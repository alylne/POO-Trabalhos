class Representacoes:

    def printDecimal(self, n):
        print(n,'\t', end='')

    def printBinario(self, n):
        print(bin(n), '\t', end='')

    def printOctal(self, n):
        print(oct(n), '\t', end='')

    def printHexadecimal(self, n):
        print(hex(n), '\t', '\n')

    def imprimirTabela(self):
        for n in range(0, 256):
            self.printDecimal(n)
            self.printBinario(n)
            self.printOctal(n)
            self.printHexadecimal(n)


print("decimal binario octa hexa")
rep = Representacoes()
rep.imprimirTabela()