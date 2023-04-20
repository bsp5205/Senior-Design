/**
 * DNA.java
 *
 * class that reads a DNA strand
 *
 * @author Kenneth Burt
 */
public class DNA {
    public String dna;
    public String header;
    private PCRList PCRL; //the full PCRList

    /**
     * the DNA constructor
     * @param header
     * @param dna
     */
    DNA(String header, String dna){
        this.dna = sanitizeDNA(dna);
        this.header = header;
    }
    /**
     * returns the header string
     * @return header
     */
    String getHeader(){
        return header;
    }

    /**
     * returns the sanitized DNA string
     * @return saniDNA
     */
    String getDNASequence(){
        return dna;
    }

    /**
     * method to return the list of protein coding regions
     * @return proteinCode
     */
    PCRList getPCRs(){
        PCRL = new PCRList();

        String frameOne = findFrameOne();
        String frameTwo = findFrameTwo();
        String triplet; //current triplet being analyzed

        boolean coding = false;
        String codeRegion = "";

        //for loop to get the PCR's of the original strand
        for(int i = 0; i < dna.length() - 2; i+=3){
            triplet = dna.substring(i, i + 3);
            if(triplet.equals("ATG")){
                coding = true;
            }

            if(coding){
                codeRegion = codeRegion + triplet;
            }

            else{
                codeRegion = "";
            }

            if(coding && (triplet.equals("TAA") ||
                    triplet.equals("TGA") ||
                    triplet.equals("TAG"))){
                coding = false;
                PCRL.add(codeRegion);
            }
        }

        if(coding){
            PCRL.add(codeRegion);
            coding = false;
            codeRegion = "";
        }

        //for loop to get the PCR's of the first frame
        for(int i = 0; i < frameOne.length() - 2; i+=3){
            triplet = frameOne.substring(i, i + 3);
            if(triplet.equals("ATG")){
                coding = true;
            }

            if(coding){
                codeRegion = codeRegion + triplet;
            }

            else{
                codeRegion = "";
            }

            if(coding && (triplet.equals("TAA") ||
                    triplet.equals("TGA") ||
                    triplet.equals("TAG"))){
                coding = false;
                PCRL.add(codeRegion);
            }
        }

        if(coding){
            PCRL.add(codeRegion);
            coding = false;
            codeRegion = "";
        }

        //for loop to get the PCR's of the second frame
        for(int j = 0; j < frameTwo.length() - 2; j+=3){
            triplet = frameTwo.substring(j, j + 3);
            if(triplet.equals("ATG")){
                coding = true;
            }

            if(coding){
                codeRegion = codeRegion + triplet;
            }

            else{
                codeRegion = "";
            }

            if(coding && (triplet.equals("TAA") ||
                    triplet.equals("TGA") ||
                    triplet.equals("TAG"))){
                coding = false;
                PCRL.add(codeRegion);
            }
        }

        if(coding){
            PCRL.add(codeRegion);
        }
        return PCRL;
    }

    /**
     * method to sanitize the DNA
     * only allowing the characters A,T,C and G
     * @param DNA
     * @return DNA
     */
    String sanitizeDNA(String DNA){
        for(int i = 0; i < DNA.length() - 1; i++){
            if(DNA.charAt(i) != 'A' && DNA.charAt(i) != 'T' &&
                    DNA.charAt(i) != 'G' && DNA.charAt(i) != 'C'){
                DNA = DNA.replace(DNA.charAt(i), '-');
            }
        }
        return DNA;
    }

    /**
     * method to return the first frame of the dna
     * @return frameOne
     */
    String findFrameOne(){
        String frameOne = dna.substring(1);
        while(frameOne.length()%3 != 0){
            frameOne = frameOne + "-";
        }

        return frameOne;
    }

    /**
     * method to return the second frame of the dna
     * @return frameTwo
     */
    String findFrameTwo(){
        String frameTwo = dna.substring(2);
        while(frameTwo.length()%3 != 0){
            frameTwo = frameTwo + '-';
        }
        return frameTwo;
    }
}
