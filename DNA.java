//
// DNAApp.java
// Class to read in file and find protein coding regions of a DNA strand
//
// @author Brandon Pijanowski
//
import javax.swing.text.Utilities;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class DNAApp {
    //
    // Main to read in file and create DNA objects
    // @param args
    //
    public static void main(String [] args){

        String filepath = "";
        Scanner scan = new Scanner(System.in);

        System.out.println("Please enter the file path:");
        filepath = scan.nextLine();

        File file = new File(filepath);

        int flag = 1;
        String head = "";
        String strand = "";
        String line = "";
        DNA dna1;
        String temp = "";

        try {

            Scanner scanFile = new Scanner(file);

            while(scanFile.hasNextLine()){

                line= scanFile.nextLine();
                //System.out.println("line: " + line);
                //System.out.println(line);

                if(line.contains(">") && (flag == 1)){

                    head = line;
                    //System.out.println(head);
                    strand = "";
                    flag = 0;

                    continue;
                }

                if(!line.contains(">")){
                    strand += line;
                }

                if(line.contains(">") || !scanFile.hasNextLine()){

                    String f1 = "";
                    String f2 = "";
                    temp = line;
                    System.out.println(head);
                    dna1 = new DNA(head,strand);
                    dna1.santizeDNA(dna1.dnaStrand);

                    f1 = dna1.findFrameOne(dna1.dnaStrand);
                    f2 = dna1.findFrameTwo(dna1.dnaStrand);

                    PCRList pcr = new PCRList();
                    pcr = outputCodingRegions(dna1.dnaStrand);
                    System.out.println(pcr);
                    pcr = outputCodingRegions(f1);
                    System.out.println(pcr);
                    pcr = outputCodingRegions(f2);
                    System.out.println(pcr);
                    strand = "";
                    head = temp;
                }

                //System.out.println(strand);


            }

        } catch (FileNotFoundException fnf) {

            fnf.printStackTrace();

        }



    }

    public static PCRList outputCodingRegions(String dna){
        // adds - till length is divisible by 3
        while(dna.length() % 3 != 0){
            dna += "-";
        }
        String test = "";
        PCRList pcr = new PCRList();
        int i = 0;
        int z = 0;
        String codon = "";
        int length = dna.length();

        while(i < dna.length()){ // while counter is less than the end of the strand

            codon = dna.substring(i,i+3); // loop till start codon

            if(codon.equals("ATG")){ // find start codon

                z = i; // set z to the start

                while(z < dna.length()){ // use z to loop from start(i) till finding a stop codon or till end of strand

                    codon = dna.substring(z,z+3);

                    if(codon.equals("TAG") || codon.equals("TGA") || codon.equals("TAA") || z == length - 3){

                        //if if starting pos is a start codon and there is a valid end codon or end o strand
                        if((dna.substring(i,i+3).equals("ATG")) &&
                                ((dna.substring(z,z+3).equals("TAG")) || (dna.substring(z,z+3).equals("TGA")) || (dna.substring(z,z+3).equals("TAA")) || z == length - 3)){

                            //if there is not a valid end then add the rest of the line
                            if(!((dna.substring(z,(z+3)).equals("TAG")) || (dna.substring(z,z+3).equals("TGA")) || (dna.substring(z,z+3).equals("TAA")) )
                                    && z == length - 3){

                                pcr.add(dna.substring(i,(z)));
                            }else{

                                //checks if two tart codons are right next to one another and only adds one
                                if(dna.substring(i,i+3).equals("ATG")&& dna.substring(i+3,i+6).equals("ATG")){
                                    pcr.add(dna.substring((i+3),((z+3))));
                                }else{
                                    pcr.add(dna.substring(i,(z+3)));
                                }
                            }

                        }

                        i = z+3;

                        break;

                    }

                    z+=3;
                }

            }

            i+=3;
        }
        return pcr;
    }
}
