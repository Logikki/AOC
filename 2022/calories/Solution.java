package calories;
import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Arrays;
import java.util.Scanner; // Import the Scanner class to read text files

class Solution {
    public static void main(String[] args) {
        int current = 0;
        int mostCalories = 0;
        int[] topThree = new int[] {0,0,0};
        try {
            File myObj = new File("calories/input.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
            
              String data = myReader.nextLine();
              if (data.equals("\n") || data.equals("")) { //seuraavan tontun stacki
                  Arrays.sort(topThree);
                  //check if list contains is value smaller than current value                  
                    if (topThree[0] < current) {
                      topThree[0] = current;
                    }
                
                if (current < mostCalories) {
                    current = 0;
                    continue;
                } else { 
                    mostCalories = current;
                    current = 0;
                }
              }
              else {
                current += Integer.parseInt(data);
              }
            }
            myReader.close();
            int sum = Arrays.stream(topThree)
              .sum();
            System.out.println( mostCalories);
            System.out.println(sum);
          } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }
        }
      }