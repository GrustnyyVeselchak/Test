def vse_deliteli_chisla (i):
    for i in range (1, 5):                 #(6000000,700000000):
        for j in range (1, int(i/2)+1):
            if i%j != 0:
                yield j
        yield i
print (vse_deliteli_chisla)