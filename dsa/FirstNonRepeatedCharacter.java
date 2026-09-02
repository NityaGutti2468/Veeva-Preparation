import java.util.HashMap;
import java.util.Map;

public class FirstNonRepeatedCharacter {
    public static char findFirstNonRepeated(String input) {
        Map<Character, Integer> frequency = new HashMap<>();
        for (char ch : input.toCharArray()) {
            frequency.put(ch, frequency.getOrDefault(ch, 0) + 1);
        }
        for (char ch : input.toCharArray()) {
            if (frequency.get(ch) == 1) {
                return ch;
            }
        }
        return '\0';
    }
    public static void main(String[] args) {
        String input = "swiss";
        char result = findFirstNonRepeated(input);
        System.out.println("First non-repeated character: " + result);
        // Output: w
    }
}
