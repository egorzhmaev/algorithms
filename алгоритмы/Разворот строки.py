s1 = 'asd'
s2 = 'dsa'

def is_anagramm(a, b):
    a = list(a.strip())
    b = list(b.strip())
    a.sort()
    b.sort()
    if a == b:
        return True
    else:
        return False

print(is_anagramm(s1, s2))