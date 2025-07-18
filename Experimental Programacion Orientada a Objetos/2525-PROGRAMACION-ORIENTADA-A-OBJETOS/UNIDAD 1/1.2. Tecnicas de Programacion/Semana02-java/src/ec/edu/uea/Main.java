package ec.edu.uea;

public class Main {

    public static void main(String[] args) {
        Guerrero personaje1 = new Guerrero("Guts", 20, 10, 4, 100, 4);
        Mago personaje2 = new Mago("Vanessa", 5, 15, 4, 100, 3);

        personaje1.atributos();
        personaje2.atributos();

        combate(personaje1, personaje2);
    }

    public static void combate(Personaje jugador1, Personaje jugador2) {
        int turno = 1;
        while (jugador1.estaVivo() && jugador2.estaVivo()) {
            System.out.println("========================= Turno " + turno + " =========================");
            System.out.println(">>> Accion de " + jugador1.nombre + ":");
            jugador1.atacar(jugador2);
            System.out.println(">>> Accion de " + jugador2.nombre + ":");
            jugador2.atacar(jugador1);
            turno++;
        }

        System.out.println("\n=========================== Fin ===========================");        
        if (jugador1.estaVivo()) {
            System.out.println("Ha ganado " + jugador1.nombre);
        } else if (jugador2.estaVivo()) {
            System.out.println("Ha ganado " + jugador2.nombre);
        } else {
            System.out.println("Empate");
        }
    }
}
