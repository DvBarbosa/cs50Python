greeting = input("Enter your greeting: ").strip().lower()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
#comando simples, faz o que pede e etc, nada alem.
#em resumo, se "greeting" começa com "hello", então, ele imprime 0.
#logo, se "saudação" começa com "Olá", responda $0
# senão, "saudação" começa com "H", responda com $20, independentemente do que vier depois, resulta 20
# enquanto nao for nenhuma das opçoes, responsa com $100, pois nao tem nem "hello" e nem começa com "H"