class Solution(object):
    def superPow(self, a, b):
        # mod rule:
        #  x^k ≡ y^k mod(m)
        #  x*k ≡ y*k mod(m)
        # eg. if a%m = r = r%m, then (a^k) % m = (r^k) % m
        

        # if we take pow of a and take mod, then we can do it like
        def powmod(n, p, m):
            if p == 0: return 1
            if p & 1: 
                return (n * powmod(n, p-1, m)) % m
            else:
                r = powmod(n, p/2, m)
                return (r * r) % m
        
        # eg. a^25 = (a^2)^10 * a^5
        ret = 1
        for n in b:
            ret =  (powmod(ret, 10, 1337) * powmod(a, n, 1337)) % 1337
        return ret
        
        
            
            

