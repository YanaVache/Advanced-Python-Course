def kompresja(tekst):
    result = []
    i = 0

    while i<len(tekst):
        sum = 1

        if i<len(tekst)-1:
            
            while tekst[i] == tekst[i+1]:
                sum += 1
                i += 1
                if i+1 == len(tekst)-1:
                    break
                
            
        znak = (tekst[i], sum)
        result.append(znak)
        i += 1

    return result


def dekompresja(tekst_skompresowany):
    result = ""
    for i in range(len(tekst_skompresowany)):
        result += tekst_skompresowany[i][0]*tekst_skompresowany[i][1] 
    return result


text = open("historia-roku.txt", "r")
kompr = kompresja(text.read())
print(kompr)
print(dekompresja(kompr))