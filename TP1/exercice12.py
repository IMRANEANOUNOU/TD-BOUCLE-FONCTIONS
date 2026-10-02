def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    
    u_prec = 1  
    u_cour = 1  
    
    for k in range(2, n + 1):
        u_suiv = u_prec + u_cour
        u_prec = u_cour
        u_cour = u_suiv
        
    return u_cour



def calcul_v(n):
    return fibonacci(n + 1) * fibonacci(n - 1) - fibonacci(n)**2
