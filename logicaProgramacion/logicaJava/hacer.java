
package logicaJava;

import java.util.Scanner;


public class hacer {
    public static void main(String [] args){
        int i, estudiantes=0;
        float promedio = 0, nota;
        Scanner captura = new Scanner(System.in);
        do {
            System.out.println("Digite la nota: ");
            nota = captura.nextFloat();
            promedio = promedio + nota;
            estudiantes++;
            System.out.println("Digite 1 para agregar otra nota o 0 para salir");
            i = captura.nextInt();
        }while(i == 1);
        promedio = promedio / estudiantes;
        System.out.println("El promedio del estudiante es: " + promedio);
    }
    
}
