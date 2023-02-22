import java.io.*;
import java.util.Map;
import java.util.Set;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class kolme {
 
    // main driver method
    public static void main(String[] args) throws Exception
    {
        Map<Integer, ArrayList<Integer>> map = new HashMap<Integer, ArrayList<Integer>>();
        BufferedReader br = filu();
        String st;
    while ((st = br.readLine()) != null) {
        for (int i=0; i < st.length(); ++i) {
            try {
                map.get(i).add(Character.getNumericValue(st.charAt(i)));
            } catch(Exception e) {
                ArrayList<Integer> lista = new ArrayList<>();
                lista.add(Character.getNumericValue(st.charAt(i)));
                map.put(i, lista);
            }
        }
    }
    String gamma = "";
    String epsilon = "";
    String oxgen = "";
    String co2 = "";
    
    for (int i : map.keySet()) {
        Integer[] arr = new Integer[map.get(i).size()];
        arr = map.get(i).toArray(arr);
        gamma += mode(arr);
        epsilon += mode(arr) ^ 1;
    }
    System.out.println("EKA:" + "\n" + "gamma" + "=" + Integer.parseInt(gamma, 2) + "\n" + "epsilon" + "=" + Integer.parseInt(epsilon, 2));
    System.out.println("tulo" + "=" + Integer.parseInt(gamma, 2) * Integer.parseInt(epsilon, 2) + "\n" + "TOKA:");
    System.out.println((kaks(map))); 
    Integer eka = Integer.parseInt("011111110111", 2);
    Integer toka = Integer.parseInt("111001000001", 2);
    System.out.println(eka*toka);

    }

    public static String kaks(Map<Integer, ArrayList<Integer>> map) {
        while (true) {
        for (int i : map.keySet()) {
        Integer moodi = mode2(map.get(i),false);
        //if (moodi == vahiten) {moodi = 1;}
        ArrayList<Integer> Indeksit = new ArrayList<>();
        //jos j paikassa ei moodia niin poistetaan ne rivit
        //listataan on indeksit jotka lisätään         
            for (int j = 0; j < map.get(i).size(); ++j) {
                if (map.get(i).get(j) == moodi) { // avaimenIndeksi = alunperin iteroitava j = listassa iteroitava
                    Indeksit.add(j);
                }
                else {
                    continue;
                }
    }
    
   
    //löydeetty indeksit, nyt poistetaan hashmapista kaikista listoista indeksin perusteella

    for (int avain : map.keySet()){
        ArrayList<Integer> lista = new ArrayList<>();
        if ((map.get(avain)).size() == 1) {
            return palautus(map);
        }
        else {
            for (int t = 0; t < Indeksit.size(); ++t){
                lista.add(map.get(avain).get(Indeksit.get(t)));
                }
        }
        try {
        map.replace(avain, lista);
        } catch(Exception e) {System.out.println("ongelma");}
    }
        }
    }
        
    }
        // Integer vastaKohtaMoodista = vahiten(arr, true);
        // Integer kuinkaMontaVastakohtaa = vahiten(arr, false);

    
        
    public static String palautus(Map<Integer, ArrayList<Integer>> map) {
        String palautus = "";
        for (int key : map.keySet()) {
            palautus += map.get(key).get(0);
        }
        return palautus;
    }
    public static int mode(Integer[] array) {
        int mode = array[0];
        int maxCount = 0;
        for (int i = 0; i < array.length; i++) {
            int value = array[i];
            int count = 0;
            for (int j = 0; j < array.length; j++) {
                if (array[j] == value) count++;
                if (count > maxCount) {
                    mode = value;
                    maxCount = count;
                    }
                }
        }
        if (maxCount > 1) {
            return mode;
        }
        return 0;
    }
    public static int mode2(ArrayList<Integer> lista, boolean eniten) {
        Integer nolla = 0;
        Integer yksi = 0;

        for (int i = 0; i < lista.size(); ++i) {
            if (lista.get(i) == 1) {
                yksi += 1;
            }
            else {
                nolla += 1;
            }
        }

        if (eniten) {
            if (yksi > nolla || yksi == nolla) {
                return 1;
            } else {
                return 0;
            }  
        }
        else {
            if (yksi > nolla || yksi == nolla) {
                return 0;
            }
                else {
                    return 1;
                }
            }
        }
    
   
     static BufferedReader filu() throws Exception{
     File file = new File(
        "input.txt");

    BufferedReader br
        = new BufferedReader(new FileReader(file));
    return br;
    
     }
}

