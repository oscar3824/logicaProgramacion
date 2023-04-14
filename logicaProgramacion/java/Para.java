
package java;

import java.util.Scanner;

/**
 *
 * @author OSCAR
 */
public class Para {
    public static void main(String [] args){
        int i, estudiantes;
        float promedio = 0, nota;
        Scanner captura = new Scanner(System.in);
        System.out.println("Digite la cantidad de estudiantes");
        estudiantes = captura.nextInt();

        for(i=0;i < estudiantes;i++){
            System.out.println("Digite la nota del estudiante: ");
            nota = captura.nextFloat();
            promedio = promedio + nota;
        }
        promedio = promedio / estudiantes;
        System.out.println("El promedio de los estudiantes es: " + promedio);
    }
    
}
