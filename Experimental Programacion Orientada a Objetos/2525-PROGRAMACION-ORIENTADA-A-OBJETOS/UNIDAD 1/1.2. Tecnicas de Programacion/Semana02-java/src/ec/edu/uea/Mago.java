package ec.edu.uea;

class Mago extends Personaje {
    private int libro;

    public Mago(String nombre, int fuerza, int inteligencia, int defensa, int vida, int libro) {
        super(nombre, fuerza, inteligencia, defensa, vida);
        this.libro = libro;
    }

    @Override
    public void atributos() {
        super.atributos();
        System.out.println("- Libro: " + libro);
    }

    @Override
    public int dano(Personaje enemigo) {
        return this.inteligencia * this.libro - enemigo.defensa;
    }
}