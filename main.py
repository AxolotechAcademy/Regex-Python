#importando el modulo para trabajar con expresiones regulares
import re

#----- MATCH - Encontrar coincidencias
string = '3314589633'
res = re.match(r'33\d{8}', string)

if res:
    print("Se encontraron coincidencias.")
else:
    print("No hay coincidencias")



#----- SEARCH
#Dos argumentos: El patron y el string.
#Busca en la primera ubicacion donde la Regex coincida con el string.

string = "Chelsae: aol.com|Dorie: 4shared.com|Felipe: nhs.uk|Ahmed: technorati.com|Davie: amazon.com|Egon: google.it"

res = re.search(r'\bD\w+', string)

#---GROUP
# Retorna la parte del string en donde se encontró coincidencia.
print(res.group())

txt = "987984519563224"
x = re.search(r'(\d{3})(\d{4})', txt)

print(x.group(2))

#---SPAN
#Retorna una tupla conteniendo el indice del comienzo y final de la parte con coincidencia
print(x.span(2))



#----- FINDALL
#Retorna una lista de strings conteniendo todas las coincidencias encontradas
string = "Nissie: A+, Devland: AB+, Wallie: AB-, Thaine: O+, Herrick: A+, Patsy: B+, Corella: A-, Avis: O-, Windy: A+"

res = re.findall( 'A[+-]', string )

print(res)




#----- SPLIT 
# separa el string en donde encuentra una coincidencia
# Y retorna una lista de todos esos strings en donde las divisiones ocurrieron.
string = "Chelsae: aol.com|Doria: 4shared.com|Felipe: nhs.uk|Ahmed: technorati.com|Davie: amazon.com|Egon: google.it"

res = re.split(r'\|', string, 3)

print(res)

print(res[2])


#----- SUB
# En base a un patron, retorna un string donde se realizaron el remplazo con el contenido especificado 
# buscar y remplazar
string = 'Este es\nun tutorial\nde python'

#print(string)

remplazo = ' '

res = re.sub(r'\n', remplazo, string)
print(res)

#Realiza un remplazo
res = re.sub(r'\n', remplazo, string, 1)
print(res)


#retorna una tupla el nuevo string con los remplazos hechos y el numero total de remplazos 
res = re.subn(r'\n', remplazo, string)
print(res)