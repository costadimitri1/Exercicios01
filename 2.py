# conversao_temperatura.py
# Entrada de dados
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Conversão para Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Exibição do resultado
print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")