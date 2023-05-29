print("Amount Due: ")

amount_due = 50
coins_added = 0

while True:
  insert_coin = int(input("Insert Coin: "))
  if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
    amount_due -= insert_coin
    coins_added += insert_coin
  else:
    print(f"Amount Due: {amount_due}")

  if coins_added >= 50:
    print(f"Change Owed: {coins_added - 50}")
    break
  else:
    print(f"Amount Due: {amount_due}")
#Eita bichinho que deu trabalho hein, foi cada correção, foi barra de espaço, mas oh, deu certo