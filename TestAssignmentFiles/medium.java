import test;
class Vehicle {
    // Vehicle attribute
    protected String brand = "Ford";

    // Vehicle method
    private void honk() {
        System.out.print("Tuut, tuut!");
    }

    public void drive() {
        System.out.print("Vroom!");
    }
}

class Car extends Vehicle {
    // Car attribute
    private String modelName = "Mustang";
    public String name = 'Bessie';
}

class notTest extends test {
    @Override
    void hey() {
        int a = 5;
    }
}

public class simple {
    public static void main(String args[]) {
        // Create a myCar object
        Car myCar = new Car();

        // Call the honk() method
        myCar.honk();

        // Display the value of the brand attribute
        System.out.println(myCar.brand + " " + myCar.modelName);

        int a = 1, b = 2, c = 3;

        if (a == 10) {
            if (b > c) {
                a = b;
            } else if (a == 5){
                a = c;
            } else {
                System.out.println(a + b + c);
            }
        }

        if (a == 10) {
            if (b > c) {
                a = b;
            } else if (a == 5){
                a = c;
            } else {
                System.out.println(a + b + c);
            }
        }

        if (a == 10) {
            if (b > c) {
                a = b;
            } else if (a == 5){
                a = c;
            } else {
                System.out.println(a + b + c);
            }
        }

        if (a == 10) {
            if (b > c) {
                a = b;
            } else if (a == 5){
                a = c;
            } else {
                System.out.println(a + b + c);
            }
        }

        if (a == 10) {
            if (b > c) {
                a = b;
            } else if (a == 5){
                a = c;
            } else {
                System.out.println(a + b + c);
            }
        }

        if (a == 10) {
            if (b > c) {
                a = b;
            } else if (a == 5){
                a = c;
            } else {
                System.out.println(a + b + c);
            }
        }

        if(a == 10) {
        }

        System.out.println(a + b + c);

        for(int i = 0; i < 5; i++) {
            System.out.println(a + b + c);
        }
    }
}