"""Time complexity notes (refactored from original exercise_5.py)

"کوییز"
for i in range(n):
    for j in range(i,n,1):
        k=p 
        print(k)
        print(p)

n+(n-1)+(n-2)+...+1
1 + 2 + 3 + ...+ n 
(n+1)+(n+1)+(n+1)+...+(n+1)
= n (n+1) / 2

F(n) = 3/2(n)(n+1)
     = 1.5 n**2 + 1.5 n
"""