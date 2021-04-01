def n_primos(n):
     i=2
     primo=0
     j=1
     while i <= n:
          while j <= n:
               if i % j == 0:
                    primo = primo + 1
               j = j + 1
               
          if primo == 2:
               print(i)
          primo=0
          i = i + 1
          j = 1
     
    
