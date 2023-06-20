from scipy.stats import poisson

# Defina o parâmetro lambda da distribuição de Poisson
lambda_ = 10

# Calcule a probabilidade de obter um determinado número de ocorrências
k = 12
probabilidade = poisson.pmf(k, lambda_)

print(f"A probabilidade de obter {k} ocorrências é: {probabilidade:.4f}")
