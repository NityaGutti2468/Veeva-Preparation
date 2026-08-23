import java.util.LinkedHashMap;
import java.util.Locale;
import java.util.Map;

public class ColorFrequencyCounter {
    public static Map<String, Integer> countColors(String input) {
        Map<String, Integer> frequency = new LinkedHashMap<>();

        if (input == null || input.isBlank()) {
            return frequency;
        }

        for (String item : input.split(",")) {
            String color = item.trim().toLowerCase(Locale.ROOT);

            // A color name must contain letters only. Numbers and symbols are ignored.
            if (color.matches("[a-z]+")) {
                frequency.put(color, frequency.getOrDefault(color, 0) + 1);
            }
        }
        return frequency;
    }

    public static void main(String[] args) {
        System.out.println(countColors(" red, blue, green, yellow, red, green, red"));
        // {red=3, blue=1, green=2, yellow=1}
    }
}
