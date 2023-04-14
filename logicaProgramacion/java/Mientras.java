
package java;

import java.util.Scanner;

/**
 *
 * @author OSCAR
 */
public class Mientras {
    public static void main(String [] args){
        int i, estudiantes;
        float promedio = 0, nota;
        Scanner captura = new Scanner(System.in);
        System.out.println("Digite la cantidad de estudiantes");
        estudiantes = captura.nextInt();
        i=0;
        while(i < estudiantes){
            System.out.println("Digite la nota del estudiante: ");
            nota = captura.nextFloat();
            promedio = promedio + nota;
            i++;
        }
        promedio = promedio / estudiantes;
        System.out.println("El promedio de los estudiantes es: " + promedio);
    }
}

