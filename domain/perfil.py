from domain.competencia import Competencia

class Perfil:
    def __init__(self, nome: str):
        self.nome = nome
        self.competencias: list[Competencia] = []

    def adicionar_competencia(self, competencia: Competencia):
        self.competencias.append(competencia)

    def obter_competencia(self, nome: str):
        for c in self.competencias:
            if c.nome == nome:
                return c
        return None

    def listar_competencias(self):
        return self.competencias

    def __repr__(self):
        return f"Perfil({self.nome})"
