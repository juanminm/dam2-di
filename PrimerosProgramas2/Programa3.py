'''
Created on 2 oct. 2017

@author: juamar
'''
def test_bob(string):
    length = len(string)
    contador = 0
    
    for i in range(0, length - 2):
        if (string[i] == string[i + 2] == "b" and string[i + 1] == "o"):
            contador += 1

    return contador
            

print(test_bob("azcbobobegghakl"))
print(test_bob("dawodwbobdiwjiwbobdiwwjamwnwbob"))
print(test_bob("bobobobobob"))
print(test_bob("his name is bob dylan"))