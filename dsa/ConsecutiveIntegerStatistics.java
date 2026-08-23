import java.util.ArrayList;
import java.util.List;

public class ConsecutiveIntegerStatistics {
    public static Result findSumAndAverage(String input) {
        List<Integer> numbers = new ArrayList<>();
        int index = 0;

        while (index < input.length()) {
            char current = input.charAt(index);
            boolean startsNumber = Character.isDigit(current)
                    || ((current == '-' || current == '+')
                    && index + 1 < input.length()
                    && Character.isDigit(input.charAt(index + 1)));

            if (!startsNumber) {
                index++;
                continue;
            }

            int sign = 1;
            if (current == '-' || current == '+') {
                sign = current == '-' ? -1 : 1;
                index++;
            }

            int value = 0;
            while (index < input.length() && Character.isDigit(input.charAt(index))) {
                value = value * 10 + (input.charAt(index) - '0');
                index++;
            }
            numbers.add(sign * value);
        }

        int sum = numbers.stream().mapToInt(Integer::intValue).sum();
        double average = numbers.isEmpty() ? 0.0 : (double) sum / numbers.size();
        return new Result(sum, average);
    }

    public record Result(int sum, double average) { }

    public static void main(String[] args) {
        System.out.println(findSumAndAverage("abc20de+30")); // Result[sum=50, average=25.0]
    }
}
