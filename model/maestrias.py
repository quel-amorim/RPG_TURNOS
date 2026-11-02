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
        self.limitadorUp = 100

    def exibirAtributos(self):
        print('-------- {self.nome} Atributos ---------\n')
        print(f'    VIT : {self.atributos['vitalidade']}')
        print(f'    STR : {self.atributos['forca']}')
        print(f'    RES : {self.atributos['defesa']}')
        print(f'    AG : {self.atributos['agilidade']}')
        print(f'    INT : {self.atributos['inteligencia']}')

    def sistemaUP(self):
        if self.xpAtual > self.limitadorUp:
            print('+1 Nivel')
            self.nivel +=1
            self.limitadorUp += 100

        return self.nivel

class Lutador(Maestria):
    def __init__(self):
        super().__init__("Lutador")

class Mago(Maestria):
    def __init__(self):
        super().__init__("Mago")

class Arqueiro(Maestria):
    def __init__(self):
        super().__init__("Arqueiro")


gerencimentoMaestria = []

l1 = Lutador()
m1 = Mago()
a1 = Arqueiro()

gerencimentoMaestria.append(l1)
gerencimentoMaestria.append(m1)
gerencimentoMaestria.append(a1)

for maestria in gerencimentoMaestria:
    print(f' & {maestria.nome} Nv {maestria.nivel}')