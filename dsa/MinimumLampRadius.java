import java.util.Arrays;

public class MinimumLampRadius {
    public static int findMinimumRadius(int[] houses, int[] lamps) {
        if (lamps.length == 0) {
            throw new IllegalArgumentException("At least one lamp is required");
        }

        Arrays.sort(lamps);
        int answer = 0;

        for (int house : houses) {
            int position = Arrays.binarySearch(lamps, house);
            if (position >= 0) {
                continue;
            }

            int insertionPoint = -position - 1;
            int leftDistance = insertionPoint > 0
                    ? house - lamps[insertionPoint - 1] : Integer.MAX_VALUE;
            int rightDistance = insertionPoint < lamps.length
                    ? lamps[insertionPoint] - house : Integer.MAX_VALUE;

            answer = Math.max(answer, Math.min(leftDistance, rightDistance));
        }
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(findMinimumRadius(new int[]{1, 2, 3}, new int[]{1, 4})); // 1
    }
}
