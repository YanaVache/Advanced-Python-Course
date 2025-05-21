def vat_faktura(lista):
    sum = 0
    vat=0.23
    for x in lista:
        sum += x
    return sum*vat
    
def vat_paragon(lista):
    sum = 0
    vat=0.23
    for x in lista:
        sum += x * vat
    return sum

zakupy = [0.2, 0.5, 4.59, 6]
print(vat_faktura(zakupy) == vat_paragon(zakupy)) #false

import decimal as d

def dec_vat_faktura(lista):
    sum = d.Decimal('0')
    vat = d.Decimal('0.23')
    for x in lista:
        sum += x
    return sum*vat
    
def dec_vat_paragon(lista):
    sum = d.Decimal('0')
    vat = d.Decimal('0.23')
    for x in lista:
        sum += x * vat
    return sum

zakupy = [d.Decimal('0.2'), d.Decimal('0.5'), d.Decimal('4.59'), d.Decimal('6')]
print(dec_vat_faktura(zakupy) == dec_vat_paragon(zakupy)) #true

# Reprezentacja liczb za pomocą klasy Decimal daje inną odpowiedź
