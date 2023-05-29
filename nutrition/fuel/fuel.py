while True:
    try:
        frac = input("Digite a fração da quantidade de combustível no tanque (no formato X/Y): ")
        X, Y = frac.split('/')
        X = int(X)
        Y = int(Y)
        if X <= 0 or Y <= 0 or X > Y:
            print("E")
        else:
            percent = round(X/Y * 100)
            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print("{:.0f}%".format(percent))
            break
    except (ValueError, ZeroDivisionError):
        print("E")

