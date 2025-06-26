package data;
import java.util.Scanner;
class EvenOdd {
    // This method checks if a number is even or odd
    // It returns true if the number is even, false if it is odd

    public static boolean isEven(int num) {
        return num % 2 == 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        int number = scanner.nextInt();
        if (isEven(number)) {
            System.out.println(number + " is even number.");
        } else {
            System.out.println(number + " is odd number.");
        }
        scanner.close();
    }

    
}