/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package java;

import java.util.Scanner;

/**
 *
 * @author OSCAR
 */
public class vector {
    public static void main(String [] args){
        // declaración de  variable del tipo arreglo
        String[] productos = new String[10];
        int i=0;
        Scanner scanner = new Scanner(System.in);
        // lee e ingresa productos al arreglo
        while (i<5) {
            System.out.print("Ingrese producto :");
            productos[i] = scanner.next(); //ingresa dato
            i++;
        }
        // Muestra las notas del arreglo
        i=1;
        while (i<=5) {
            System.out.println("Producto "+ i +" " + productos[i-1]);
            i++;
        }
    } 
}
