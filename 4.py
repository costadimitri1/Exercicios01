# salario_mensal.py
# Entrada de dados
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
valor_hora = float(input("Digite o valor recebido por hora: "))

# Cálculo do salário
salario = horas_trabalhadas * valor_hora

# Exibição do resultado
print(f"O salário total do mês é: R$ {salario:.2f}")