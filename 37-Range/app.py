"""
for + range
- iteravel
range -> range(start, stop, step)
"""

for i in range(0, 10, 1): # desconsidera o 10
    print(i)

print("-" * 15)

texto = "Gabriel"

for i in range(0, len(texto)):
    print(texto[i])