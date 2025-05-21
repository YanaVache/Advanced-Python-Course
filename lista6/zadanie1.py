import requests
import re 

adres = '([a-zA-Z]+.)*[a-zA-Z]+'
automat_https = re.compile('https://'+ adres)

url = 'https://skos.ii.uni.wroc.pl/course/view.php?id=406'

was_already = set()
ans = []

def crawl(start_page, distance, action):
    req = requests.get(start_page, 'html.parser')
    text = req.text
    ans.append((start_page, action(text)))
    if distance > 1:
        for i in [url.group() for url in automat_https.finditer(text)]:
            if i not in was_already:
                was_already.add(i)
                crawl(i, distance - 1, action)
    

def how_many_pythons(text):
    res = 0
    for sentence in text.split('.'):
        if 'python' in sentence.lower():
            res += 1
    return res

crawl(url, 2, how_many_pythons)
print(ans)