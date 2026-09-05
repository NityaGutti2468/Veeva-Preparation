import java.util.Scanner;
public class FibonacciPreviousNext {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int a = 0, b = 1;
        int previous = -1;
        int next = -1;
        while (b <= n) {
            previous = b;
            int c = a + b;
            a = b;
            b = c;
        }
        next = b;
        System.out.println("Previous Fibonacci number: " + previous);
        System.out.println("Next Fibonacci number: " + next);
        sc.close();
    }
}
