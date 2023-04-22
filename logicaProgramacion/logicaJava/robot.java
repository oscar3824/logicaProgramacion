package logicaJava;

    import java.util.Scanner;

    public class robot {
      public static int maxInstructions() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese los planes de movimiento del robot (L, R, U, D): ");
        String plans = sc.nextLine();
        sc.close();
    
        int minX = 0, minY = 0;
        int x = 0, y = 0;
        for (char c : plans.toCharArray()) {
          if (c == 'L') {
            x--;
          } else if (c == 'R') {
            x++;
          } else if (c == 'U') {
            y++;
          } else if (c == 'D') {
            y--;
          }
          minX = Math.min(minX, x);
          minY = Math.min(minY, y);
        }
        return Math.abs(minX) + Math.abs(minY);
      }
    }
    

