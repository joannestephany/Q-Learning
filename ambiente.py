import numpy as np

quantidadeLinhasAmbiente = 6
quantidadeColumasAmbiente = 6

tabela_qsa = np.zeros((quantidadeLinhasAmbiente, quantidadeColumasAmbiente, 4))

acoesDisponiveis = ['cima', 'baixo', 'esquerda', 'direita']

tabelaRecompensas = np.full((quantidadeLinhasAmbiente, quantidadeColumasAmbiente), 0.)
tabelaRecompensas[5, 5] = 10.

print(tabelaRecompensas)
