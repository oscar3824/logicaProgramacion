
package logicaJava;


public class Switch {
    public static void main(String[] args){
        String    nombreDia = "";
        int dia = 8;
        switch (dia) {
             case 1: nombreDia ="Lunes";
             break;
             case 2: nombreDia ="Martes";
             break;
             case 3: nombreDia ="Miércoles";
             break;
             case 4: nombreDia ="Jueves";
             break;
             case 5: nombreDia ="Viernes";
             break;
             case 6: nombreDia ="Sábado";
             break;
             case 7: nombreDia ="Domingo";
             break;
             default: System.out.println("Error, el valor no corresponde a ningun dia de la semana");
          }
        if (nombreDia != ""){
          System.out.println("El día " + dia + "es " + nombreDia);
        }
    }
    
}
 