class TortugasNinja:
    # atributos/propiedades
    poderAtaque = 100
    poderDefensa = 90
    agilidad = 100
    puntosVida = 200
    vidas = 3
    velocidad = 300
    arma = ""

    # metodos
    def ataque(self):
        print("ataca")

    def defensa(self):
        print("Defiende")

# objeto
Donatello = TortugasNinja()
Donatello.arma = "Bo"
print(f'el poder de ataque de donatello es {Donatello.poderAtaque} y su arma es {Donatello.arma}')

#objeto2
Maiky = TortugasNinja()
Maiky.arma = "chacos"
print(f'el poder de ataque de Maiky es {Maiky.poderAtaque} y su arma es {Maiky.arma}')

enemigoCerca = input("¿esta Destructor cerca?")
if enemigoCerca == "si":
    print('Donatelo')
    Donatello.defensa()
    
    print('Maiky')
    Maiky.ataque()

