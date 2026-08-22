import java.util.ArrayList;
import java.util.List;

public class FindAllAnagramsInAString {
    public static List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();

        if (p.length() > s.length()) {
            return result;
        }

        int[] required = new int[26];
        int[] window = new int[26];

        for (int i = 0; i < p.length(); i++) {
            required[p.charAt(i) - 'a']++;
            window[s.charAt(i) - 'a']++;
        }

        if (matches(required, window)) {
            result.add(0);
        }

        for (int right = p.length(); right < s.length(); right++) {
            window[s.charAt(right) - 'a']++;
            window[s.charAt(right - p.length()) - 'a']--;

            if (matches(required, window)) {
                result.add(right - p.length() + 1);
            }
        }

        return result;
    }

    private static boolean matches(int[] first, int[] second) {
        for (int i = 0; i < 26; i++) {
            if (first[i] != second[i]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(findAnagrams("cbaebabacd", "abc")); // [0, 6]
    }
}
