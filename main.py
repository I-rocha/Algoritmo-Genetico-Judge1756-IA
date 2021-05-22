# input
def this_input(T, bits, corte, prob, X, Y, obj):
    for i in range(T):
        bits.append(int(input()))
        _in = input().split()
        corte.append(int(_in[0]))
        prob.append(float(_in[1]))
        X.append(str(input()))
        Y.append(str(input()))
        obj.append(str(input()))

# Crossover por par de individuo
def crossOver(X, Y, corte):
    newX = []
    newY = []

    newX = X[:corte] + Y[corte:len(Y)]
    newY = Y[:corte] + X[corte:len(X)]
    
    return newX, newY

# Distancia do objetivo
def erro(E, obj):
    erroE = 0
    
    for i in range(len(obj)):
        if(E[i] != obj[i]):
            erroE += 1
        
    return erroE

# Prob de 1 estado atingir objetivo
def probObj(erros, acertos, p_mutacao):
    p_nMutacao = 1 - p_mutacao
    
    probManter = (p_nMutacao ** acertos)
    probMudar = (p_mutacao ** erros)
    
    return (probManter * probMudar)

# Probabilidade da uniao
def probAuB(pA, pB):
    return pA + pB - (pA * pB)

def main():
    T = int(input()) # Numero de casos teste

    # Vetor para cada caso Teste
    bits = []    # Qtd de bits
    corte = []   # Posicao de corte
    prob = []    # Probabilidade de ocorrencia
    X = []       # Individuo 1
    Y = []       # Individuo 2
    obj = []     # Individuo objetivo

    this_input(T, bits, corte, prob, X, Y, obj)

    for i in range(T):
        # CrossOver
        filhoA, filhoB = crossOver(X[i], Y[i], corte[i])

        # Erros
        erroA = erro(filhoA, obj[i])
        erroB = erro(filhoB, obj[i])

        # Probabilidade por cadeia
        probA = probObj(erroA, bits[i] - erroA, prob[i])
        probB = probObj(erroB, bits[i] - erroB, prob[i])

        # Probabilidade total
        prob_sucesso = float(probAuB(probA, probB))

        print(f'{prob_sucesso:.7f}')
        
main()
