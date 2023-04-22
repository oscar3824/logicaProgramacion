
package logicaJava;

import java.util.Scanner;

public class Notas {
    public static void main (String [] args){
         float notas;
         Scanner captura = new Scanner(System.in);
         System.out.println("Digite la nota final de la asignatura: ");
         notas = captura.nextFloat();
         if(notas < 0 || notas > 5){
            System.out.println("Por favor digite un numero entre 0 y 5");
         }
         else{
            if(notas < 2){
                System.out.println("Peerdio!!!!!");
            }
            else{
                if(notas < 3){
                    System.out.println("Pilas!!!! tiene que recuperar");
                }
                else{
                    System.out.println("FELICITACIONES!!! Aprobó");
                    }
            
                }
    
            }
    }
}

