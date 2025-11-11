
#E = 0+ 1+ 4+ 9+ 16+ 25+ 36+⋯ 
import math
E=0
qt=int(input("introduza o nr de termos"))
for i in range(0,qt+1):
    E+=(math.pow(i,2))
    
    
print(f"A soma dos termos desssa serie: {E} ")