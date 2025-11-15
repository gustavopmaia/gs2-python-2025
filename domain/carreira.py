class Carreira:
    def __init__(self, nome: str, requisitos: dict):
        self.nome = nome
        self.requisitos = requisitos # logica, programacao, criatividade, etc.

    def __repr__(self):
        return f"Carreira: {self.nome}"
