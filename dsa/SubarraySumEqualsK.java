import java.util.HashMap;
import java.util.Map;

public class SubarraySumEqualsK {
    public static int countSubarrays(int[] numbers, int k) {
        Map<Integer, Integer> prefixFrequency = new HashMap<>();
        prefixFrequency.put(0, 1);

        int prefixSum = 0;
        int count = 0;

        for (int number : numbers) {
            prefixSum += number;
            count += prefixFrequency.getOrDefault(prefixSum - k, 0);
            prefixFrequency.put(prefixSum,
                    prefixFrequency.getOrDefault(prefixSum, 0) + 1);
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(countSubarrays(new int[]{1, 2, 3}, 3)); // 2
    }
}
