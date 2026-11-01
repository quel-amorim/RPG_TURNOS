class Maestria:
    def __init__(self,nomeMaestria):
        self.nome = nomeMaestria
        self.nivel = 1
        self.atributos = {
            'vitalidade' : 10,
            'forca' : 10,
            'defesa' : 10,
            'agilidade' : 10,
            'inteligencia' : 10
        }
        self.xpAtual = 0

    def exibirAtributos(self):
        print('-------- {self.nome} Atributos ---------\n')
        print(f'    VIT : {self.atributos['vitalidade']}')
        print(f'    STR : {self.atributos['forca']}')
        print(f'    RES : {self.atributos['defesa']}')
        print(f'    AG : {self.atributos['agilidade']}')
        print(f'    INT : {self.atributos['inteligencia']}')

    def sistemaUP(self):
        if self.xpAtual > 100:
            print('+1 Nivel')
            self.nivel +=1
            self.xpAtual = 0

        return self.nivel