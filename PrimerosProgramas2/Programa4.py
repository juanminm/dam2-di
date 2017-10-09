'''
Created on 2 oct. 2017

@author: juamar
'''
def item_order (orden):
    ensaladas = orden.count("ensalada") 
    hamburguesas = orden.count("hamburguesa") 
    agua = orden.count("agua") 

    print("ensaladas:", ensaladas, "hamburguesas:", hamburguesas, "agua:", agua)
        
item_order("ensalada hamburguesa agua ensalada hamburguesa")
item_order("hamburguesa hamburguesa agua")        