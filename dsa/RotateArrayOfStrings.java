import java.util.Arrays;
public class RotateArrayOfStrings {
    public static void rotate(String[] arr, int k) {
        int n = arr.length;
        k = k % n;
        reverse(arr, 0, n - 1);
        reverse(arr, 0, k - 1);
        reverse(arr, k, n - 1);
    }
    private static void reverse(String[] arr, int left, int right) {
        while (left < right) {
            String temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }
    public static void main(String[] args) {
        String[] arr = {"apple", "banana", "orange", "mango", "grapes"};
        int k = 2;
        rotate(arr, k);
        System.out.println(Arrays.toString(arr));
    }
}
