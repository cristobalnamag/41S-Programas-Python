class TortugasNinja:
    # atributos/propiedades
    def __init__(self, nombre, ataque, defensa, vida, arma, vidas):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        self.arma = arma 
        self.vidas = vidas


    # metodos
    def ataque(self):
        print("ataca")

    def defensa(self):
        print("Defiende")

# objeto
Donatello = TortugasNinja("Donatello",100, 120, 200, "Bo", 3)
print(f'{Donatello.nombre} tiene {Donatello.ataque} puntos de ataque y su arma es {Donatello.arma}')

Maiky = TortugasNinja("Maiky",90, 120, 130, "chacos", 3)
print(f'{Maiky.nombre} tiene {Maiky.ataque} puntos de ataque y su arma es {Maiky.arma}')

Rafa = TortugasNinja("Rafa",130, 150, 140, "Sai", 3)
print(f'{Rafa.nombre} tiene {Rafa.ataque} puntos de ataque y su arma es {Rafa.arma}')

Leo = TortugasNinja("Leo",120, 100, 200, "Katana", 3)
print(f'{Leo.nombre} tiene {Leo.ataque} puntos de ataque y su arma es {Leo.arma}')

Spike = TortugasNinja("Spike", 115, 120, 130, "acha", 1)
print(f'{Spike.nombre} tiene {Spike.ataque} puntos de ataque y su arma es {Spike.arma}')

if Donatello.ataque > Spike.ataque:
    print("gana Donatello")

else:
    Donatello.vidas -= 1
    print(Donatello.vidas)