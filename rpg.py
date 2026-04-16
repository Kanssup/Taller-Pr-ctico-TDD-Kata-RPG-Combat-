class Personaje:
    def __init__(self):
        self.hp = 1000
        self.nivel = 1
        self.esta_vivo = True

def test_personaje_recibe_dano():
    heroe = Personaje()
    enemigo = Personaje()
    
    # Act (Actuar)
    enemigo.atacar(heroe, dano=200)
    
    # Assert
    assert heroe.hp == 800

