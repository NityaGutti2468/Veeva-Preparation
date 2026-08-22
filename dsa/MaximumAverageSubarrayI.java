public class MaximumAverageSubarrayI {
    public static double findMaxAverage(int[] nums, int k) {
        int windowSum = 0;

        for (int i = 0; i < k; i++) {
            windowSum += nums[i];
        }

        int maximumSum = windowSum;

        for (int right = k; right < nums.length; right++) {
            windowSum += nums[right];
            windowSum -= nums[right - k];
            maximumSum = Math.max(maximumSum, windowSum);
        }

        return (double) maximumSum / k;
    }

    public static void main(String[] args) {
        int[] nums = {1, 12, -5, -6, 50, 3};
        System.out.println(findMaxAverage(nums, 4)); // 12.75
    }
}
