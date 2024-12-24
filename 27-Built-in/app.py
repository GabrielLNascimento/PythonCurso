"""
imutaveis: str, bool, int, float
"""

#         0123456
string = "Gabriel"

# string[3] = "ABC" -> erro
# nao consigo alterar os valores dessa variavel - imutavel

# jeito alternativo para alterar
outra_string = f"{string[:3]}ABC{string[4:]}"

print(string)
print(outra_string)



