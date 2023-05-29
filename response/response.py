from validator_collection import validators

def main():
    # Solicita o endereço de e-mail ao usuário
    email_address = input("What's your email address? ")

    # Validação de e-mail
    try:
        emailIsValid = validators.email(email_address)
        # Validação de domínio
        domainIsValid = validators.domain(email_address.split('@')[1])
        if emailIsValid and domainIsValid:
            print("Valid")
        else:
            print("Invalid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()
