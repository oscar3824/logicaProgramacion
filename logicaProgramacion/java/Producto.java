/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package java;

import java.util.ArrayList;
import java.util.Scanner;

/**
 *
 * @author OSCAR
 */
/*public class Producto {
    //Atributos
    //public tipoDato nombre;
    private int codigo;
    private String descripcion;
    private float valorUnitario;

    //Constructores sobrecargados
    public Producto(int c,String d, float v){
        this.codigo = c;
        this.descripcion = d;
        this.valorUnitario = v;
    }
    public Producto(){
        this.codigo = 0;
        this.descripcion = "";
        this.valorUnitario = 0;
    }
    public Producto(String c,String d, String v){
        this.codigo = Integer.parseInt(c);
        this.descripcion = d;
        this.valorUnitario = Float.parseFloat(v);
    }
    //Get and Sed
    public int getCodigo(){
        return this.codigo;
    }
    public void setCodigo (int codigo){
        this.codigo=codigo;
    }
    public String getDescripcion(){
        return this.descripcion;
    }
    public void setDescripcion (String descripcion){
        this.descripcion=descripcion;
    }
    public float getValorUnitario(){
        return this.valorUnitario;
    }
    public void setValorUnitario (float ValorUnitario){
        this.valorUnitario=ValorUnitario;
    }
    //METODO PRINCIPAL
    public static void main(String [] args){
        ArrayList <Producto> listadoProductos = new ArrayList<Producto>();
        Producto p1 = new Producto(10,"Papa",1000);
        p1.mostrarse();
        Scanner captura = new Scanner(System.in);
        System.out.println("Digite el codigo del producto");
        int d1 = captura.nextInt();
        System.out.println("Digite la descripción del producto");
        String d2 = captura.next();
        System.out.println("Digite el valor unitario del producto");
        float d3 = captura.nextFloat();
        Producto p2 = new Producto(d1,d2,d3);
        p2.mostrarse();
        Producto p3 = new Producto();
        p3.mostrarse();
        p3.setCodigo(10);
        p3.setDescripcion("Arroz");
        p3.setValorUnitario(1500);
        p3.mostrarse();
        Producto p4 = new Producto("2","Zapatos", "300000");
        p4.mostrarse();
        System.out.println(p4.toString());
        System.out.println("El valor de 2 pares de zapatos es: " + p4.calcularPrecio(2));
    }

    public void mostrarse(){
        System.out.println("Codigo: " + this.codigo + " \nDescripcion: " + this.descripcion + " \nValor unitario: " + this.valorUnitario);
    }
    public String toString(){
        return "Codigo: " + this.getCodigo() + " \nDescripcion: " + this.getDescripcion() + " \nValor unitario: " + this.getValorUnitario();
    }
    public float calcularPrecio(int cantidad){
        return cantidad * this.valorUnitario;
    }

}*/
