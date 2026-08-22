# Veeva Optimized Coding Set - Java

This sheet contains optimized Java solutions for the coding problems shared for Veeva preparation.

## 1. Make String a Subsequence Using Cyclic Increments

Pattern: Two pointers

Idea: Each character in `str1` can either stay same or increment once cyclically. So `str1[i]` can match `str2[j]` if:

- `str1[i] == str2[j]`
- or next cyclic character of `str1[i]` equals `str2[j]`

```java
class Solution {
    public boolean canMakeSubsequence(String str1, String str2) {
        int j = 0;

        for (int i = 0; i < str1.length() && j < str2.length(); i++) {
            char current = str1.charAt(i);
            char next = current == 'z' ? 'a' : (char) (current + 1);

            if (current == str2.charAt(j) || next == str2.charAt(j)) {
                j++;
            }
        }

        return j == str2.length();
    }
}
```

Time: O(n)  
Space: O(1)

## 2. Invalid Transactions

Pattern: String parsing + comparison

Standard LeetCode rule: A transaction is invalid if:

- amount > 1000
- or same name has another transaction within 60 minutes in a different city

```java
import java.util.*;

class Solution {
    static class Transaction {
        String original;
        String name;
        int time;
        int amount;
        String city;

        Transaction(String transaction) {
            original = transaction;
            String[] parts = transaction.split(",");
            name = parts[0];
            time = Integer.parseInt(parts[1]);
            amount = Integer.parseInt(parts[2]);
            city = parts[3];
        }
    }

    public List<String> invalidTransactions(String[] transactions) {
        int n = transactions.length;
        Transaction[] arr = new Transaction[n];

        for (int i = 0; i < n; i++) {
            arr[i] = new Transaction(transactions[i]);
        }

        boolean[] invalid = new boolean[n];

        for (int i = 0; i < n; i++) {
            if (arr[i].amount > 1000) {
                invalid[i] = true;
            }

            for (int j = i + 1; j < n; j++) {
                if (arr[i].name.equals(arr[j].name)
                        && !arr[i].city.equals(arr[j].city)
                        && Math.abs(arr[i].time - arr[j].time) <= 60) {
                    invalid[i] = true;
                    invalid[j] = true;
                }
            }
        }

        List<String> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (invalid[i]) {
                result.add(arr[i].original);
            }
        }

        return result;
    }
}
```

Time: O(n^2)  
Space: O(n)

Note: This is accepted because constraints are small in the original problem.

## 3. Subarrays With K Different Integers

Pattern: Sliding window + HashMap

Formula:

```text
exactly(k) = atMost(k) - atMost(k - 1)
```

```java
import java.util.*;

class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        return atMost(nums, k) - atMost(nums, k - 1);
    }

    private int atMost(int[] nums, int k) {
        if (k == 0) return 0;

        HashMap<Integer, Integer> map = new HashMap<>();
        int left = 0;
        int count = 0;

        for (int right = 0; right < nums.length; right++) {
            map.put(nums[right], map.getOrDefault(nums[right], 0) + 1);

            while (map.size() > k) {
                map.put(nums[left], map.get(nums[left]) - 1);
                if (map.get(nums[left]) == 0) {
                    map.remove(nums[left]);
                }
                left++;
            }

            count += right - left + 1;
        }

        return count;
    }
}
```

Time: O(n)  
Space: O(k)

## 4. Shortest Path in Binary Matrix

Pattern: BFS in 8 directions

```java
import java.util.*;

class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;

        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) {
            return -1;
        }

        int[][] dirs = {
            {-1, -1}, {-1, 0}, {-1, 1},
            {0, -1},           {0, 1},
            {1, -1},  {1, 0},  {1, 1}
        };

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0, 1});
        grid[0][0] = 1;

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int r = curr[0];
            int c = curr[1];
            int dist = curr[2];

            if (r == n - 1 && c == n - 1) {
                return dist;
            }

            for (int[] d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];

                if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                    grid[nr][nc] = 1;
                    q.add(new int[]{nr, nc, dist + 1});
                }
            }
        }

        return -1;
    }
}
```

Time: O(n^2)  
Space: O(n^2)

## 5. Find All Duplicates in an Array

Pattern: Index marking / sign marking

Condition: numbers are in range `[1, n]`, each appears at most twice.

```java
import java.util.*;

class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            int index = Math.abs(nums[i]) - 1;

            if (nums[index] < 0) {
                result.add(index + 1);
            } else {
                nums[index] = -nums[index];
            }
        }

        return result;
    }
}
```

Time: O(n)  
Extra Space: O(1), excluding output

## 6. Duplicate Objects in an Array of Objects

In Java, represent each object as a `User`. Duplicate is based on `name + email`.

Pattern: HashMap with composite key

```java
import java.util.*;

class User {
    int id;
    String name;
    String email;

    User(int id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }

    public String toString() {
        return id + " " + name + " " + email;
    }
}

class Main {
    public static void main(String[] args) {
        User[] users = {
            new User(1, "Amit Kumar", "amit@example.com"),
            new User(2, "Sumit Kumar", "sumit@example.com"),
            new User(3, "Amit Kumar", "amit@example.com"),
            new User(4, "Raj Kumar", "raj@example.com"),
            new User(5, "Amit Kumar", "amit@example.com")
        };

        HashMap<String, List<User>> map = new HashMap<>();

        for (User user : users) {
            String key = user.name + "#" + user.email;
            map.putIfAbsent(key, new ArrayList<>());
            map.get(key).add(user);
        }

        List<User> duplicates = new ArrayList<>();

        for (List<User> group : map.values()) {
            if (group.size() > 1) {
                duplicates.addAll(group);
            }
        }

        for (User user : duplicates) {
            System.out.println(user);
        }
    }
}
```

Time: O(n)  
Space: O(n)

## 7. Duplicates in Limited Range and Limited Repetition Array

Same optimized idea as Problem 5.

```java
import java.util.*;

class Main {
    public static void main(String[] args) {
        int[] arr = {2, 3, 1, 2, 3};
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            int index = Math.abs(arr[i]) - 1;

            if (arr[index] < 0) {
                result.add(index + 1);
            } else {
                arr[index] = -arr[index];
            }
        }

        System.out.println(result);
    }
}
```

Time: O(n)  
Extra Space: O(1), excluding output

## 8. Longest Increasing Subsequence

Optimized pattern: Binary search + tails array

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;

        for (int x : nums) {
            int left = 0;
            int right = size;

            while (left < right) {
                int mid = left + (right - left) / 2;

                if (tails[mid] < x) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }

            tails[left] = x;

            if (left == size) {
                size++;
            }
        }

        return size;
    }
}
```

Time: O(n log n)  
Space: O(n)

## 9. LIS in Circular Manner

Constraints: `N <= 300`, so O(n^3) is acceptable.

Idea:

- Try every starting position.
- Build the circular array of length n from that start.
- Compute normal LIS using O(n^2).
- Take maximum.

```java
public class Solution {
    public static int lisInCircularManner(int n, int[] arr) {
        int answer = 1;

        for (int start = 0; start < n; start++) {
            int[] circular = new int[n];

            for (int i = 0; i < n; i++) {
                circular[i] = arr[(start + i) % n];
            }

            int[] dp = new int[n];
            for (int i = 0; i < n; i++) {
                dp[i] = 1;
            }

            int best = 1;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < i; j++) {
                    if (circular[j] < circular[i]) {
                        dp[i] = Math.max(dp[i], dp[j] + 1);
                    }
                }
                best = Math.max(best, dp[i]);
            }

            answer = Math.max(answer, best);
        }

        return answer;
    }
}
```

Time: O(n^3)  
Space: O(n)

Since n is only 300, this is safe for the given constraints.

## 10. Minimum Loss From Buying and Selling Once

Problem: Given prices on each day, buy once and sell once later. Find minimum possible loss.

Important: Buy day must come before sell day. Loss means buy price > sell price and loss = buy - sell.

Examples:

```text
[6, 8, 10, 4, 9] -> 1
Buy at 10, sell at 9, loss = 1

[8, 9, 3, 5] -> 3
Buy at 8, sell at 5, loss = 3
```

Optimized approach: TreeSet

While scanning prices from left to right, `TreeSet` stores previous buy prices. For current sell price, find the smallest previous price greater than current price.

```java
import java.util.*;

class Main {
    public static void main(String[] args) {
        int[] prices = {6, 8, 10, 4, 9};

        TreeSet<Integer> previousPrices = new TreeSet<>();
        int minLoss = Integer.MAX_VALUE;

        for (int price : prices) {
            Integer higher = previousPrices.higher(price);

            if (higher != null) {
                minLoss = Math.min(minLoss, higher - price);
            }

            previousPrices.add(price);
        }

        System.out.println(minLoss);
    }
}
```

Time: O(n log n)  
Space: O(n)

## Quick Pattern Summary

1. Cyclic subsequence - Two pointers
2. Invalid transactions - Parsing + comparison
3. Subarrays with K distinct - Sliding window
4. Binary matrix shortest path - BFS
5. Duplicates in range 1 to n - Sign marking
6. Duplicate objects - HashMap composite key
7. Limited range duplicates - Sign marking
8. LIS - Binary search
9. Circular LIS - Try all rotations + LIS DP
10. Minimum loss - TreeSet
