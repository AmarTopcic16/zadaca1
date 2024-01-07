def brisem_grad():
    file = open('gl_gradovi.txt', 'r')
    y = file.read()
    x = y.split(', ')
    file.close()

    grad = input('Unesi naziv glavnog grada koji zelis da izbrises: ')

    if any(s.lower() == grad.lower() for s in x):
        z = [i for i in x if i.lower() != grad.lower()]

        file = open('gl_gradovi.txt', 'w')
        file.write(", ".join(z))
        file.close()
    else:
        print("Nema ga na spisku")
    
def dodajem_grad():
    file = open('gl_gradovi.txt', 'r')
    y = file.read()
    x = y.strip().split(', ')
    file.close()

    grad = str(input('Unesi naziv grada koji zelis da dodas: '))

    if grad in x:
        print("Grad vec postoji u listi")
    else:
        if x and not x[-1]:
            x[-1] = grad 
        else:
            x.append(grad)

    file = open('gl_gradovi.txt', 'w')
    file.write(", ".join(x))
    file.close()

file = open('gl_gradovi.txt', 'r')
y = file.read()
x = y.strip().split(', ')
file.close()

print("--------------------------------------------------------------------")
print("Glavni gradovi koji se trenutno nalaze na listi su: ")
print(*x, sep=", ") 
print("--------------------------------------------------------------------")
print("Da li zelite unijeti novi glavni grad ili obrisati postojeci(1/2): ")
print("1. Unijeti novi")
print("2. Obrisati postojeci")
odabir = int(input("Vas odabir(1/2): "))

if odabir==1:
    dodajem_grad()
elif odabir==2:
    brisem_grad()
else:
    print("Pogresan unos")

