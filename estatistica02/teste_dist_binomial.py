from scipy.stats import binom

n = 12  # número total de questões
p = 1/4  # probabilidade de acertar cada questão (1/4 = 0.25)

probabilidade = binom.pmf(7, n, p)
print("Probabilidade de acertar exatamente 7 questões:", probabilidade)
