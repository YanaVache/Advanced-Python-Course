def is_palindrom(text):
    a=''
    text = text.lower()
    for r in text:
        if r.isalpha() is True:
            a+=r
    rev_text = a[::-1] 
    return a == rev_text


print(is_palindrom("Eine güldne, gute Tugend: Lüge nie!"))
print(is_palindrom("Míč omočím."))
print(is_palindrom("rotor"))
print(is_palindrom("Kobyła ma mały bok."))
print(is_palindrom("kar tar"))
print(is_palindrom("Как там?"))
