class Competencia:
    def __init__(self, nome: str, tipo: str, nivel: int):
        self.nome = nome
        self.tipo = tipo # Pode ser hard skill ou soft skill
        self.nivel = nivel

    def __repr__(self):
        return f"{self.nome.capitalize()} ({self.tipo}) - Nível {self.nivel}"
