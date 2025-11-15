class Recomendador:
    def __init__(self, carreiras):
        self.carreiras = carreiras

    def avaliar(self, perfil):
        resultados = []

        for carreira in self.carreiras:
            total = 0
            atendidas = 0
            faltantes = []

            for req, nivel_req in carreira.requisitos.items():
                comp = perfil.obter_competencia(req)

                if comp:
                    total += comp.nivel
                    if comp.nivel >= nivel_req:
                        atendidas += 1
                    else:
                        faltantes.append((req, nivel_req - comp.nivel))
                else:
                    faltantes.append((req, nivel_req))

            score = atendidas / len(carreira.requisitos)

            resultados.append({
                "carreira": carreira.nome,
                "score": score,
                "faltantes": faltantes
            })

        resultados.sort(key=lambda x: x["score"], reverse=True)
        return resultados
