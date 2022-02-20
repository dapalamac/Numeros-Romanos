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

num = 'III'

nuevalista = [str(a) for a in str(num)]
print('-----proceso1-----')
print(nuevalista)

print('-----proceso2-----')

sum = 0

listarenovada = []
for x in nuevalista:
    
    
    print(numrom[x])
    
    listarenovada.append((numrom[x]))
    
    sum = sum + int(numrom[x])

 
print('-----proceso3-----')  

print(sum)

print('-----proceso4-----')  

res = 0

for i in range (len(listarenovada)):
    
    if int(listarenovada[0]) < int(listarenovada[1]):
        
       sum = -(int(listarenovada[0]) - int(listarenovada[1]))
    
    elif int(listarenovada[0]) >= int(listarenovada[1]):
        
       sum = int(listarenovada[0]) + int(listarenovada[1])
       
       
       
       
    elif int(listarenovada[1]) < int(listarenovada[2]):
        
        sum = (int(listarenovada[0]) + int(listarenovada[1])) - (int(listarenovada[2]))
        
    elif int(listarenovada[1]) >= int(listarenovada[2]):
        
        sum = int(listarenovada[0]) + int(listarenovada[1]) + int(listarenovada[2])
        
        
        
        
  
    elif int(listarenovada[2]) < int(listarenovada[3]):
        
        sum = (int(listarenovada[0]) + int(listarenovada[1])+ int(listarenovada[2])) - (int(listarenovada[3]))
        
    elif int(listarenovada[2]) >= int(listarenovada[3]):
        
        sum = int(listarenovada[0]) + int(listarenovada[1])+ int(listarenovada[2]) + int(listarenovada[3])
        
    
    elif int(listarenovada[3]) < int(listarenovada[4]):
        
        sum = (int(listarenovada[0]) + int(listarenovada[1])+ int(listarenovada[2])+ int(listarenovada[3])) - (int(listarenovada[4]))
        
    elif int(listarenovada[3]) >= int(listarenovada[4]):
        
        sum = (int(listarenovada[0]) + int(listarenovada[1])+ int(listarenovada[2])+ int(listarenovada[3]) + int(listarenovada[4]))
                                                                  
                                                                  
                                                                  
   
                                                               

 

                                                               
                                                               
                                                               
                                                               
        
    # elif int(listarenovada[3]) < int(listarenovada[4]):
        
    #     sum = (int(listarenovada[0]) + int(listarenovada[1])+ int(listarenovada[2])+ int(listarenovada[3])) - (int(listarenovada[4])) 
        
    # elif int(listarenovada[4]) < int(listarenovada[5]):
        
    #     sum = (int(listarenovada[0]) + int(listarenovada[1])+ int(listarenovada[2])+ int(listarenovada[3])+ int(listarenovada[4])) - (int(listarenovada[5])) 
    
    
print(sum)
    
   
        
        
        
        
         
         
         





    
    

    


