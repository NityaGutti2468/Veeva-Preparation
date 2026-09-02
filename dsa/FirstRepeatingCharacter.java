import java.util.HashMap;
import java.util.Map;

public class FirstRepeatingCharacter {
    public static int findFirstRepeating(String input) {
        Map<Character, Integer> frequency = new HashMap<>();
        for (char ch : input.toCharArray()) {
            frequency.put(ch, frequency.getOrDefault(ch, 0) + 1);
        }
        for (int i = 0; i < input.length(); i++) {
            if (frequency.get(input.charAt(i)) > 1) {
                return i;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        String input = "swiss";
        int index = findFirstRepeating(input);
        System.out.println("First repeating character index: " + index);
        // Output: 0
    }
}
