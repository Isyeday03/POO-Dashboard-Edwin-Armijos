package ec.edu.uea;

class Personaje {
    protected String nombre;
    protected int fuerza;
    protected int inteligencia;
    protected int defensa;
    protected int vida;

    public Personaje(String nombre, int fuerza, int inteligencia, int defensa, int vida) {
        this.nombre = nombre;
        this.fuerza = fuerza;
        this.inteligencia = inteligencia;
        this.defensa = defensa;
        this.vida = vida;
    }

    public void atributos() {
        System.out.println(nombre + ":");
        System.out.println("- Fuerza: " + fuerza);
        System.out.println("- Inteligencia: " + inteligencia);
        System.out.println("- Defensa: " + defensa);
        System.out.println("- Vida: " + vida);
    }

    public void subirNivel(int fuerza, int inteligencia, int defensa) {
        this.fuerza += fuerza;
        this.inteligencia += inteligencia;
        this.defensa += defensa;
    }

    public boolean estaVivo() {
        return vida > 0;
    }

    public void morir() {
        vida = 0;
        System.out.println(nombre + " ha muerto");
    }

    public int dano(Personaje enemigo) {
        return this.fuerza - enemigo.defensa;
    }

    public void atacar(Personaje enemigo) {
        int daño = this.dano(enemigo);
        enemigo.vida -= daño;
        System.out.println(nombre + " ha realizado " + daño + " puntos de danio a " + enemigo.nombre);
        if (enemigo.estaVivo()) {
            System.out.println("Vida de " + enemigo.nombre + " es " + enemigo.vida);
        } else {
            enemigo.morir();
        }
    }
}