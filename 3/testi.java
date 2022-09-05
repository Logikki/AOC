import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class testi {
    public static void main(String[] args) {
    Map<Integer, ArrayList<String>> map = new HashMap<Integer, ArrayList<String>>();
    for (Integer i =0; i<5; ++i) {
        ArrayList<String> lista = new ArrayList<String>();
        lista.add(i.toString());
        lista.add(i.toString());
        lista.add(i.toString());
        lista.add(i.toString());
        lista.add(i.toString());
        lista.add(i.toString());
        map.put(i,lista);
        
    }
    System.out.println(map);   
    map.get(0).remove(100);
    System.out.println(map);
    }
}
