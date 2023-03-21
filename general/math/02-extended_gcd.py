# p = 26513
# q = 32321
# u, v = 0

# ns + at = 1 

'''
 function inverse(a, n)
    t := 0;     newt := 1
    r := n;     newr := a

    while newr ≠ 0 do
        quotient := r div newr
        (t, newt) := (newt, t - quotient * newt) 
        (r, newr) := (newr, r - quotient * newr)

    if r > 1 then
        return "a is not invertible"
    if t < 0 then
        t := t + n

    return t
'''

def inverse(p, q):
    if p == 0 :
        return q, 0, 1
             
    gcd,x1,y1 = inverse(q % p, p)
     
    x = y1 - (q//p) * x1
    y = x1
     
    return gcd, x, y

print(inverse(32321, 26513))