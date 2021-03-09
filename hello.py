def juft(x):
    return x%2 == 0

sonlar = [1, 2, 3 , 4, 5, 6, 7, 8, 8, 9, 0, 19, 20, 22, 14]

juftlar = list(filter(juft, sonlar))

print(juftlar)