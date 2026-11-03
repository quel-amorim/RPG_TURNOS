from random import randint,choices
class Mob:
    def __init__(self,nomeMob):
        self.nome = nomeMob
        self.nivel = 1
        self.atributos = {
            'vitalidade' : 10,
            'forca' : 10,
            'defesa' : 10,
            'agilidade' : 10,
            'inteligencia' : 10
        }
        self.xpDrop = randint(1, 20)
        self.chanceDrops()
        self.moedaDrop()

    def exibirAtributos(self):
            print(f'-------- {self.nome} Atributos ---------\n')
            print(f'    VIT : {self.atributos['vitalidade']}')
            print(f'    STR : {self.atributos['forca']}')
            print(f'    RES : {self.atributos['defesa']}')
            print(f'    AG : {self.atributos['agilidade']}')
            print(f'    INT : {self.atributos['inteligencia']}')

    def chanceDrops(self):
        drops = ['Essencia de Monstro','Espada','Machado']
        return f"{self.nome} dropou {choices(drops,weights=[70 , 15 , 15])}"

    def moedaDrop(self):
        moedas = randint(1,35)
        return f"Você ganhou {moedas} moedas !"


class Zumbi(Mob):
     def __init__(self):
          super().__init__("Zumbi")
          self.atributos['vitalidade'] -= 7
          self.atributos['forca'] += 5
          self.atributos['defesa'] -= 6
          self.atributos['agilidade'] -= 8
          self.atributos['inteligencia'] -= 9

class Demonio(Mob):
     def __init__(self):
          super().__init__("Demônio")
          self.atributos['vitalidade'] += 8
          self.atributos['forca'] += 8
          self.atributos['defesa'] += 8
          self.atributos['agilidade'] += 8
          self.atributos['inteligencia'] += 8

class Anjo(Mob):
     def __init__(self):
          super().__init__("Anjo")
          self.atributos['vitalidade'] += 5
          self.atributos['forca'] += 5
          self.atributos['defesa'] += 5
          self.atributos['agilidade'] += 5
          self.atributos['inteligencia'] += 5


z1 = Zumbi()
d1 = Demonio()
a2 = Anjo()

gerenciamentoMobs = []
gerenciamentoMobs.append(z1)
gerenciamentoMobs.append(d1)
gerenciamentoMobs.append(a2)

for mob in gerenciamentoMobs:
    print(f' & {mob.nome} Nv {mob.nivel} | Drop XP : {mob.xpDrop}')

z1.exibirAtributos()
print()
d1.exibirAtributos()
print()
a2.exibirAtributos()