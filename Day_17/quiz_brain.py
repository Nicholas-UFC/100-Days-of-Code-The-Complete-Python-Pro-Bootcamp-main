from data import question_bank


class QuizBrain:
    def __init__(self, lista_de_questao) -> None:
        self.numero_da_questao = 0
        self.pontos = 0
        self.lista_de_questao = lista_de_questao

    def comecar_as_perguntas(self):
        print(
            "Vamos começar as perguntas, responda True ou False, cada resposta correta é 1 ponto e cada resposta errada é 0 pontos."
        )

        for i in range(len(self.lista_de_questao)):
            resposta = str(input((f"Q{i + 1}: {self.lista_de_questao[i].pergunta}: ")))
            resposta = resposta.strip().capitalize()

            if resposta == self.lista_de_questao[i].resposta:
                self.pontos += 1
