from scipy.stats import chi2_contingency

# Dados observados
observado = [[41, 34], [18, 7]]

# Realize o teste de Qui-Quadrado
estatistica, p_valor, graus_liberdade, esperado = chi2_contingency(observado)

print("Estatística Qui-Quadrado:", estatistica)
print("Valor p:", p_valor)
print("Graus de liberdade:", graus_liberdade)
print("Tabela de frequências esperadas:", esperado)
