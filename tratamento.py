from ambiente import *


def verificarEstadoFinal(actual_line, actual_column):
    if tabelaRecompensas[actual_line, actual_column] == 0.:
        return False
    else:
        return True


def posicaoAleatoria():  # define uma posição inicial aleatória
    linhaAtual = np.random.randint(quantidadeLinhasAmbiente)
    columaAtual = np.random.randint(quantidadeColumasAmbiente)
    while verificarEstadoFinal(linhaAtual, columaAtual):
        linhaAtual = np.random.randint(quantidadeLinhasAmbiente)
        columaAtual = np.random.randint(quantidadeColumasAmbiente)

    return linhaAtual, columaAtual


def proximaAcao(actual_line, actual_column, eps):
    if np.random.random() < eps:  #se o numero aleatório for menor que o epsilon, a gente troca pra um valor melhor
        return np.argmax(tabela_qsa[actual_line, actual_column])
    else:  # segue pelo numero aleatório sorteado, já que é maior que epsilon
        return np.random.randint(4)


def proximaPosicao(linhaAtual, columaAtual, action):
    proximaLinha, proximaColuna = linhaAtual, columaAtual

    if acoesDisponiveis[action] == 'cima' and linhaAtual > 0:
        proximaLinha -= 1
    elif acoesDisponiveis[action] == 'baixo' and linhaAtual < quantidadeLinhasAmbiente - 1:
        proximaLinha += 1
    elif acoesDisponiveis[action] == 'esquerda' and columaAtual > 0:
        proximaColuna -= 1
    elif acoesDisponiveis[action] == 'direita' and columaAtual < quantidadeColumasAmbiente - 1:
        proximaColuna += 1
    return proximaLinha, proximaColuna


def shortest_path(linhaInicial, colunaInicial):
    if verificarEstadoFinal(linhaInicial, colunaInicial):
        return []
    else:
        linhaAtual, columaAtual = linhaInicial, colunaInicial
        path = []
        path.append([linhaAtual, columaAtual])

        while not verificarEstadoFinal(linhaAtual, columaAtual):
            acao = proximaAcao(linhaAtual, columaAtual, 1.)
            linhaAtual, columaAtual = proximaPosicao(linhaAtual, columaAtual, acao)
            path.append([linhaAtual, columaAtual])
    return path
