Godown_A=list(map(str,input('Enter the produc codes : ').split()))
Godown_B=list(map(str,input('Enter the product codes : ').split()))
print('Unified Invertory : ',set(Godown_A+Godown_B))