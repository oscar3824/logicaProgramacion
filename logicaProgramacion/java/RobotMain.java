package java;

public class RobotMain {
    public static void main(String[] args) {
        Robot robot = new Robot();
        int result = robot.maxInstructions();
        System.out.println("El número máximo de instrucciones es: " + result);
      }
    }