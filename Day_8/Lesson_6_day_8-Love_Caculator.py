def calculate_love_score(name1, name2):
    nome = name1 + name2
    lower_nome = nome.lower()

    T = lower_nome.count('t')
    R = lower_nome.count('r')
    U = lower_nome.count('u')
    E = lower_nome.count('e')
    primeiro_digito = T+R+U+E

    L = lower_nome.count('l')
    O = lower_nome.count('o')
    V = lower_nome.count('v')
    segundo_digito = L+O+V+E

    score = str(primeiro_digito) + str(segundo_digito)
    score = int(score)

    if score<10 or score>90:
        print(f'Your score is {score}, you go together like coke and mentos.')

    elif score>=40 and score<=50:
        print(f'Your score is {score}, you are alright together.')
    else:
        print(f'Your score is {score}.')

calculate_love_score(name1 = "Bryan Nicholas", name2 = "Maria Rita")