num_user = input("Digite um número: ")

num_user = int(num_user)

if num_user > 100:
    print("Seu número é muito grande")
elif num_user > 50:
    print("Seu número ta na média")
else:
    print("Seu número é muito pequeno")