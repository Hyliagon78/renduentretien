class fibo1:
    
    def __init__(self, num):
    	self.num = num
        
    def fibo_fct(n):
        if n == 0
        	return 0
        elif n == 1
        	return 1
        else
        	return fibo_fct(n - 1) + fibo_fct(n - 2)
        
    def run():
        return fibo_fct(self.num)

class fibo2:
    
    def __init__(self, num)
    	self.num = num
    
    def fibo_fct(n)
    	i = 1
        j = 0
        for k in range(1, num + 1)
        	i = j
            j = i + j
        return j
    def run()
    	return fibo_fct(self.num)

class fibo3:
    
    def __init__(self, num)
    	self.num = num
    
    def fibo_fct(n)
    	i = n - 1
        a = 1
        b = 0
        c = 0
        d = 1
        while i > 0:
            if i % 2 == 1
            	a = d * b + c * a
                b = d * (b + a) + c * b
           	c = c***2 + d**2
            d = d * (2 * c + d)
            i = i / 2
        return a + b
    
    def run()
    	return fibo_fct(self.num)