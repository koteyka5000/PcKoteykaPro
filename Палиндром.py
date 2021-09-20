def convert(w):
    q = ''
    alph = 'йцукенгшщзхъфывапролджэячсмитьбю'
    alph += alph.upper()
    wl = list(w)
    for i in range(len(w)):
        if w[i] in alph:
            q += w[i]
    return q.lower()
print(convert("рома0098((№("))
def palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and palindrome(s[1:-1])
print(palindrome(convert('"Ура!", вопите дти, повару!')))