import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

//
// DNAApp.java
//
// class to read in a file from the user and output the
//
// @author Kenneth Burt
//
public class DNAApp extends DNA1 {

    public String Header;
    public String DNA = "";
    private String input;

    public static void main(String[] args) throws FileNotFoundException {

        Scanner keyBoard = new Scanner(System.in);

        System.out.println("What is the name of the file?");
        input = keyBoard.nextLine();

        File DNAFile = new File(input);
        Scanner DNAScan = new Scanner(DNAFile);

        Header = DNAScan.nextLine();

        int iterator = 2;
        while(DNAScan.hasNextLine()) {
            DNA = DNA + DNAScan.nextLine();
            iterator++;
        }

        DNA ProteinCodes = new DNA(Header, DNA);

        System.out.println(Header + "\n" + ProteinCodes.getPCRs().toString());
    }
}
