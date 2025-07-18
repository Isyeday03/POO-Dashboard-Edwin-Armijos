package ec.edu.uea;

import java.util.Scanner;

class Guerrero extends Personaje {

    private int espada;

    public Guerrero(String nombre, int fuerza, int inteligencia, int defensa, int vida, int espada) {
        super(nombre, fuerza, inteligencia, defensa, vida);
        this.espada = espada;
    }

    public void cambiarArma() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Elige un arma: (1) Acero Valyrio, dano 8. (2) Matadragones, dano 10");
        int opcion = scanner.nextInt();
        if (opcion == 1) {
            espada = 8;
        } else if (opcion == 2) {
            espada = 10;
        } else {
            System.out.println("Numero de arma incorrecta");
        }
    }

    @Override
    public void atributos() {
        super.atributos();
        System.out.println("- Espada: " + espada);
    }

    @Override
    public int dano(Personaje enemigo) {
        return this.fuerza * this.espada - enemigo.defensa;
    }
}
