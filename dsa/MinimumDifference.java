import java.util.Arrays;

public class MinimumDifference {
    public static int findMinimumDifference(int[] numbers) {
        if (numbers == null || numbers.length < 2) {
            return -1;
        }

        Arrays.sort(numbers);
        int minimumDifference = Integer.MAX_VALUE;

        for (int i = 1; i < numbers.length; i++) {
            minimumDifference = Math.min(minimumDifference, numbers[i] - numbers[i - 1]);
        }
        return minimumDifference;
    }

    public static void main(String[] args) {
        System.out.println(findMinimumDifference(new int[]{10, 20, 40, 45})); // 5
    }
}
