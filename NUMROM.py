# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 18:05:29 2022

@author: dapal
"""



numrom = {
        'I': "1",
        'V': "5",
        'X': "10",
        'L': "50",
        'C': "100",
        'D': "500",
        'M': "1000",
        }  

num = 'IV'

nuevalista = [str(a) for a in str(num)]
print('-----proceso1-----')
print(nuevalista)

print('-----proceso2-----')

sum = 0
for x in nuevalista:
    
    
    print(numrom[x])
    
    sum = sum + int(numrom[x])

 
print('-----proceso3-----')  

print(sum)

    


