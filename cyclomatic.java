public class main {
    public static void main(String args[]) {
        int a = 1, b = 2, c = 3;

        if(a == 10) {
            if(b > c) {
                a = b;
            } else {
                a = c;
            }
        }

        System.out.println(a + b + c);
    }

    public static void second() {
        int a = 1, b = 2, c = 3;

        if(a == 10) {
            if(b > c) {
                a = b;
            } else {
                a = c;
            }

            if(1) {
                a = a;
            }
        }

        System.out.println(a + b + c);
    }
}