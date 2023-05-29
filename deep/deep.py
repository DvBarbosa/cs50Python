#pega a entrada
answer = input(
  "What is the answer To The Great Question of live, the universe and everything? "
)

#imprima sim se a resposta do usuario for 42, ou quarenta e dois, no caso, em ingles
if answer.strip() == "42":
  print("Yes")

elif answer.lower().strip() == "forty-two":
  print("Yes")

elif answer.lower().strip() == "forty two":
  print("Yes")

#de outra forma, diga não
else:
  print("No")
