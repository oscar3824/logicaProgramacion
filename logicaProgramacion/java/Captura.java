
package java;

import java.util.Scanner;

public class Captura {
    public static void main(String[] args){
        String producto;
        int cantidad;
        float valorUnitario;
        double valorFinal;
        Scanner captura = new Scanner(System.in);
        System.out.println("Digite el nombre del producto: ");
        producto = captura.nextLine();
        System.out.println("Digite la cantidad del producto: ");
        cantidad = captura.nextInt();
        System.out.println("Digite el valor unitario del producto: ");
        valorUnitario = captura.nextFloat();
        valorFinal = (valorUnitario * cantidad) + (valorUnitario * cantidad)*0.19;
        System.out.println("El valor de " + cantidad + producto + " es: " + valorFinal);     

    }             
}  
    
    

