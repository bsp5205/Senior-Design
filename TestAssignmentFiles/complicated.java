import test;
class Vehicle {
    // Vehicle attribute
    public String brand = "Ford";
    public int gold = 1000;

    // Vehicle method
    private void honk() {
        System.out.print("Tuut, tuut!");
    }

    // The most important method
    private void drive() {
        System.out.print("Vroom!");
    }

    // Do not  do this at all
    private void text() {
        System.out.println("You should not do this");
    }

    // Very important
    public void turn() {
        int i = 0;
        while(i < 5) {
            i++;
        }
    }
}

class Car extends Vehicle {
    // Car attribute
    public String modelName = "Mustang";
    public String name = 'Bessie';
    public int time = 24;
}

class Mazda extends Car {
    public int amount = 12000;
}

class Wheel extends Mazda {
    public String type = "offroad";
}

class Atom extends Wheel {

}

class notTest extends test {
    @Override
    private void hey() {
        int a = 5;
    }

    @Override
    public void pog() {
        int c = 6;
    }

    @Override
    public void hello() {
        String hello = "Hello";
    }

    @Override
    public void goodbye() {
        String goodbye = "Goodbye";
    }

    @Override
    public void last() {
        int b = 10;
    }

    private void dog() {
        int newVariable = 25, sum = 0;

        for(int i = 0; i < newVariable; i++) {
            sum++;
        }
    }
}

public class simple {
    public static void main(String args[]) {
        // Create a myCar object
        Car myCar = new Car();

        // Call the honk() method
        myCar.honk();
        myCar.drive();
        myCar.turn();

        test test = new test();
        test.hey();
        test.pog();
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

        try {
            int[] myNumbers = {1, 2, 3};
            System.out.println(myNumbers[10]);
        } catch (Exception e) {
            System.out.println("Something went wrong.");
        }

        int day = 4;
        switch (day) {
          case 1:
            System.out.println("Monday");
            break;
          case 2:
            System.out.println("Tuesday");
            break;
          case 3:
            System.out.println("Wednesday");
            break;
          case 4:
            System.out.println("Thursday");
            break;
          case 5:
            System.out.println("Friday");
            break;
          case 6:
            System.out.println("Saturday");
            break;
          case 7:
            System.out.println("Sunday");
            break;
        }


        if(a == 10) {
        }

        System.out.println(a + b + c);

        for(int i = 0; i < 5; i++) {
            System.out.println(a + b + c);
        }
    }
}