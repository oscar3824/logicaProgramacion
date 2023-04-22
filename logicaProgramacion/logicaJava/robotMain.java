package logicaJava;

public class robotMain {
    public static void main(String[] args) {
        robot robot = new robot();
        int result = robot.maxInstructions();
        System.out.println("El número máximo de instrucciones es: " + result);
      }
    }
    