from tratamento import *
from ambiente import *

# paramentros de treinamento
epsilon = 0.5
fatorDesconto = 0.9
TaxaAprendizagem = 0.9

for tentativa in range(1000):
    linhaNova, columaNova = posicaoAleatoria()

    while not verificarEstadoFinal(linhaNova, columaNova):
        acao = proximaAcao(linhaNova, columaNova, epsilon)

        linhaAnterior, columaAnterior = linhaNova, columaNova
        linhaNova, columaNova = proximaPosicao(linhaNova, columaNova, acao)

        recompensa = tabelaRecompensas[linhaNova, columaNova]
        q_antigo = tabela_qsa[linhaAnterior, columaAnterior, acao]
        diferencaTemporal = recompensa + (fatorDesconto * np.max(tabela_qsa[linhaNova, columaNova])) - q_antigo

        q_novo = q_antigo + (TaxaAprendizagem * diferencaTemporal)
        tabela_qsa[linhaAnterior, columaAnterior, acao] = q_novo
print("\nAprendizado completo!\n\n")