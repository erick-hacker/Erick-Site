print("=== CALCULADORA DO ERICK ===")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("\nO que quer fazer?")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

op = input("Escolha 1/2/3/4: ")

if op == "1":
    print(f"Resultado: {n1 + n2}")
elif op == "2":
    print(f"Resultado: {n1 - n2}")
elif op == "3":
    print(f"Resultado: {n1 * n2}")
elif op == "4":
    print(f"Resultado: {n1 / n2}")
else:
    print("Opção inválida!")
