from typing import List, Optional

class Material:
    def __init__(self, nome: str, lote: str, unidade_de_medida: str, quantidade: float):
        self.nome = nome
        self.lote = lote
        self.unidade_de_medida = unidade_de_medida
        self.quantidade = quantidade

    def __repr__(self):
        return f"Material(nome={self.nome}, lote={self.lote}, unidade_de_medida={self.unidade_de_medida}, quantidade={self.quantidade})"


class Receita:
    def __init__(self, id: str, responsavel: str, destino: str):
        self.id = id
        self.responsavel = responsavel
        self.destino = destino
        self.materiais_receita: List[Material] = []

    def adicionar_material(self, material: Material) -> None:
        self.materiais_receita.append(material)
        print("Material adicionado com sucesso")

    def get_receita(self):
        return {
            'id': self.id,
            'responsavel': self.responsavel,
            'destino': self.destino
        }

    def get_materiais_receita(self):
        return self.materiais_receita

material1 = Material(nome="Farinha", lote="1234", unidade_de_medida="kg", quantidade=10)
material2 = Material(nome="Água", lote="5678", unidade_de_medida="L", quantidade=5)


receita = Receita(id="001", responsavel="Carlos", destino="Panificação")


receita.adicionar_material(material1)
receita.adicionar_material(material2)


print(receita.get_receita())
print(receita.get_materiais_receita())
