"""
Fatiamento de strings

  012345678
  Ola mundo
 -987654321

fatiamento [i:f:p] [::]
i - inicio
f - fim
p - passo 

funcao len()
retorna o tamanho da variavel
"""

variavel = "ola mundo"

print(variavel[2])
print(variavel[-5])

# vai do indice 4 até o final
print(variavel[4:])

# vai do indice 4 até o indice 7, desconsidera o 7
print(variavel[4:7])

# quero que começo no zero e vá até o indice 4, omitir o inicio
print(variavel[:4]) # 4 não é incluido


