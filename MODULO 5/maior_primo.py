def éPrimo(k):
    if k < 2:
        return False
    i = 2
    while i * i <= k:  
        if k % i == 0:  
            return False  
        i += 1  
    return True  

def maior_primo(n):
    while n >= 2:  
        if éPrimo(n):  
            return n  
        n -= 1  

print(maior_primo(100))  
print(maior_primo(7))    