import math
x=0.5
epsilon=0.01
term= math.sin(x)
sum_series=term
sign=-1
n=2
while abs(term)>epsilon:
    term=(math.sin(x)**n)/n*sign
    sum_series+=term
    sign*=-1
    n+=1
print(f"sum_series:{sum_series}")
