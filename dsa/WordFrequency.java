import java.util.LinkedHashMap;
import java.util.Map;

public class WordFrequency {
    public static Map<String, Integer> countWords(String sentence) {
        Map<String, Integer> frequency = new LinkedHashMap<>();

        for (String word : sentence.toLowerCase().split("\\s+")) {
            String cleanWord = word.replaceAll("[^a-z0-9]", "");
            if (!cleanWord.isEmpty()) {
                frequency.put(cleanWord, frequency.getOrDefault(cleanWord, 0) + 1);
            }
        }
        return frequency;
    }

    public static void main(String[] args) {
        System.out.println(countWords("Hello This is India This is India"));
    }
}
