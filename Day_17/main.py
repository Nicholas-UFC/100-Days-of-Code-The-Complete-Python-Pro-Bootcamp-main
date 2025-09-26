from data import question_bank
from quiz_brain import QuizBrain

banco_de_perguntas_1 = QuizBrain(question_bank)
banco_de_perguntas_1.comecar_as_perguntas()
print(banco_de_perguntas_1.pontos)
