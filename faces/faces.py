def main():
    msg = input()
    resultado = convert(msg)
    print (resultado)

def convert(msg):
    msg1 = msg.replace(":)",'🙂')
    msg2 = msg1.replace(":(", '🙁')
    return msg2

main()