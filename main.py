class Material():

    def __init__(self, nome, lote, unidade_de_medida, quantidade):

        self.nome = nome
        self.lote = lote
        self.unidade_de_medida = unidade_de_medida
        self.quantidade = quantidade

    def adicionar_na_receita(self):

        material_adicionado = [self.nome, self.lote, self.unidade_de_medida,self.quantidade]
        return material_adicionado

class Receita():

    def __init__(self):

        self.materiais_receita = []
        
        pass
    
    def get_receita(self):

        return self.id , self.responsavel, self.destino

    def get_materiais_receita(self):

        return self.materiais_receita

    def criar_receita(self):

        id  = input("inpute o id")
        responsavel = input("inpute o responsavel")
        destino = input("inpute o destino")

        self.id = id
        self.responsavel = responsavel
        self.destino = destino

        return id , responsavel, destino 

    def adicionar_material(self, material):

        try:
            material_adicionado = material
            self.materiais_receita.append(material_adicionado)

            print("material adicionado com sucesso")
        except:

            print("material adicionado incorretamente")

sulfato_magnesio = Material("sulfato_mg", "lote1" , "kg", 500)

receita1 = Receita()

receita1.criar_receita()
receita1.adicionar_material(sulfato_magnesio)

print(receita1.get_receita())
print(receita1.get_materiais_receita())
