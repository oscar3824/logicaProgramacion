package logicaJava;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class robot2 {
public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    // Leer cantidad de planes a evaluar
    System.out.println("Digite numero planes de instruciones a ejecutar: ");
    int n = scanner.nextInt();
    scanner.nextLine();

    // Leer planes y calcular la distancia de cada uno
    List<Integer> distancias = new ArrayList<>();
    for (int i = 0; i < n; i++) {
        System.out.println("Digite plan de instrucciones: ");
        String plan = scanner.nextLine();
        int distancia = calcularDistancia(plan);
        distancias.add(distancia);

        // Calcular el número máximo de instrucciones necesarias para regresar a la base para este plan
        int maxInstrucciones = 2 * distancia; // el robot debe recorrer la misma distancia de regreso
        System.out.println(maxInstrucciones);
    }
}

private static int calcularDistancia(String plan) {
    int x = 0;
    int y = 0;
    for (char instruccion : plan.toCharArray()) {
        switch (instruccion) {
            case 'L':
                x--;
                break;
            case 'R':
                x++;
                break;
            case 'U':
                y++;
                break;
            case 'D':
                y--;
                break;
        }
    }
    return Math.abs(x) + Math.abs(y);
}
}