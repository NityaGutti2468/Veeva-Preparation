# Veeva Previous-Year Java Questions

Polished revision sheet with all options, correct answers, key explanations, and Java code for the coding questions.

## Set 1: Previous-Year Java MCQs

### 1. Encapsulation

How is encapsulation primarily achieved in Java?

A. By using public variables and public methods  
B. By using private variables and public getter/setter methods  
C. By using abstract classes only  
D. By utilizing multiple inheritance  

Answer: B  
Explanation: Encapsulation protects data by keeping variables private and providing controlled access using public getters and setters.

### 2. Interfaces

Which statement about interfaces in Java is correct?

A. An interface can contain constructors  
B. Interfaces support multiple inheritance in Java  
C. Interfaces can be instantiated directly using new  
D. Interfaces can only contain final and static methods  

Answer: B  
Explanation: A class can implement multiple interfaces, so Java supports multiple inheritance through interfaces.

### 3. Method Overloading

When does overloading not occur?

A. Same method name but different parameter number/type  
B. Same method name and same signature  
C. Same method name, same number of parameters but different type  
D. Same method name, same number and type of parameters but different signature  

Answer: B  
Explanation: Overloading requires a different parameter list. Same name and same signature is not overloading.

### 4. Inheritance

Which statement about inheritance is true?

A. A class can extend multiple classes  
B. A subclass inherits methods from superclass  
C. Inheritance can only be achieved through interfaces  
D. Constructors are inherited by subclasses  

Answer: B  
Explanation: A subclass inherits accessible methods and fields from its superclass. Constructors are not inherited.

### 5. equals()

What does equals() usually compare?

A. Object references  
B. Object content  
C. Class type only  
D. Memory address only  

Answer: B  
Explanation: equals() is intended for content comparison when properly overridden. == compares references.

### 6. hashCode()

Why override hashCode() when overriding equals()?

A. To ensure object identity  
B. To maintain hash table contract  
C. To optimize memory  
D. To allow overloading  

Answer: B  
Explanation: Equal objects must have equal hash codes for HashMap, HashSet, and other hash-based collections.

### 7. Object Class

Which is true about Object class?

A. All classes inherit from Object  
B. Object cannot be subclassed  
C. Object has no methods  
D. Object has no constructors  

Answer: A  
Explanation: Every Java class directly or indirectly inherits from Object.

### 8. protected

What is visibility of protected?

A. Same class only  
B. Same package only  
C. Same package and subclasses  
D. Everywhere  

Answer: C  
Explanation: protected members are accessible within the same package and in subclasses.

### 9. private

What is visibility of private?

A. Everywhere  
B. Same class only  
C. Subclasses only  
D. Same package only  

Answer: B  
Explanation: private members are accessible only inside the class where they are declared.

### 10. Multiple Inheritance

Which is true about multiple inheritance in Java?

A. A class can implement multiple interfaces  
B. A class can extend multiple classes  
C. Multiple inheritance is allowed for classes and interfaces  
D. A class can inherit from multiple abstract classes  

Answer: A  
Explanation: Java does not allow a class to extend multiple classes, but it can implement multiple interfaces.

### 11. Integer Cache

What is the output?

```java
Integer num1 = 100;
Integer num2 = 100;
Integer num3 = 500;
Integer num4 = 500;

System.out.println(num1 == num2);
System.out.println(num3 == num4);
```

A. true true  
B. true false  
C. false true  
D. false false  

Answer: B  
Explanation: Integer values from -128 to 127 are cached. 100 uses cache, but 500 creates separate objects.

### 12. Byte Array To String

What is the output?

```java
byte[] arr = {97, 98, 99, 100, 101};
String str = new String(arr);
System.out.println(str);
```

A. abcde  
B. 979899100101  
C. Compile-time error  
D. Runtime error  

Answer: A  
Explanation: ASCII values 97, 98, 99, 100, 101 correspond to a, b, c, d, e.

### 13. charAt()

What is the output?

```java
String str = "Java Programming";
char ch = str.charAt(2);
System.out.println(ch);
```

A. J  
B. a  
C. v  
D. P  

Answer: C  
Explanation: Indexing starts at 0. J=0, a=1, v=2.

## Set 1: Coding Questions With Java Code

### Coding 1. Closest Number To Target

Given an array and target K, return the number with the smallest absolute difference from K. If there is a tie, choose the greater number.

```java
class Main {
    public static void main(String[] args) {
        int[] arr = {9, 11, 5, 3, 25, 18};
        int k = 6;

        int closest = arr[0];
        int minDiff = Math.abs(arr[0] - k);

        for (int i = 1; i < arr.length; i++) {
            int diff = Math.abs(arr[i] - k);

            if (diff < minDiff || (diff == minDiff && arr[i] > closest)) {
                minDiff = diff;
                closest = arr[i];
            }
        }

        System.out.println(closest);
    }
}
```

Time: O(n)  
Space: O(1)

### Coding 2. Validate Subsequence

Check whether sequence is a subsequence of array. Elements must appear in the same order, but not necessarily continuously.

```java
class Main {
    public static void main(String[] args) {
        int[] array = {5, 1, 22, 25, 6, -1, 8, 10};
        int[] sequence = {1, 6, -1, 10};

        int i = 0;

        for (int x : array) {
            if (i < sequence.length && x == sequence[i]) {
                i++;
            }
        }

        System.out.println(i == sequence.length);
    }
}
```

Time: O(n)  
Space: O(1)

### Coding 3. First Non-Repeating Character

Find the first character that appears only once. If none exists, print -1.

Frequency array version for lowercase English letters:

```java
class Main {
    public static void main(String[] args) {
        String s = "loveleetcode";

        int[] freq = new int[26];

        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
        }

        for (int i = 0; i < s.length(); i++) {
            if (freq[s.charAt(i) - 'a'] == 1) {
                System.out.println(s.charAt(i));
                System.out.println(i);
                return;
            }
        }

        System.out.println(-1);
    }
}
```

HashMap version for general characters:

```java
import java.util.*;

class Main {
    public static void main(String[] args) {
        String s = "loveleetcode";

        HashMap<Character, Integer> map = new HashMap<>();

        for (char ch : s.toCharArray()) {
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (map.get(ch) == 1) {
                System.out.println(ch);
                System.out.println(i);
                return;
            }
        }

        System.out.println(-1);
    }
}
```

Time: O(n)  
Space: O(1) for frequency array, O(k) for HashMap

## Set 2: OOP Java MCQs

### 1. Interface Implementation

When a class implements an interface, which of the following must be implemented?

A. Only abstract methods  
B. Only non-abstract methods  
C. Both abstract and non-abstract methods  
D. Only static methods  

Answer: A  
Explanation: A class implementing an interface must implement its abstract methods.

### 2. Method Overriding

What happens if a method in a subclass has the same name and parameters as a method in its superclass?

A. The superclass method is executed  
B. The subclass method is executed  
C. A compile-time error occurs  
D. The program fails to run  

Answer: B  
Explanation: The subclass method overrides the superclass method.

### 3. Java Interface

Which of the following correctly describes a Java interface?

A. It can have method implementations  
B. It can contain instance variables  
C. It can extend multiple classes  
D. It can only contain abstract methods  

Answer: D  
Explanation: This is the old/basic MCQ answer. Modern Java interfaces can also have default and static methods.

### 4. Serializable

What is the purpose of the Serializable interface in Java?

A. To create a deep copy of an object  
B. To allow objects to be serialized  
C. To enable thread safety  
D. To implement cloning  

Answer: B  
Explanation: Serializable marks a class so its objects can be converted into a byte stream.

### 5. final Method

How do you prevent a method from being overridden in a subclass?

A. Declare it as final  
B. Declare it as private  
C. Declare it as static  
D. Declare it as abstract  

Answer: A  
Explanation: A final method cannot be overridden.

### 6. Multiple Interfaces

Which statement about multiple inheritance of interfaces is true?

A. It is allowed in Java  
B. It is not allowed in Java  
C. It leads to ambiguity always  
D. Only one interface can be inherited  

Answer: A  
Explanation: A class can implement multiple interfaces.

### 7. Inner Class

Which keyword is used to declare an inner class?

A. inner  
B. static  
C. public  
D. class  

Answer: D  
Explanation: Inner classes are declared with the normal class keyword.

### 8. Invalid Casting

What is the result of attempting to cast an object to a class that it does not inherit from?

A. Compile-time error  
B. Run-time exception  
C. It will return null  
D. It will create a new instance  

Answer: B  
Explanation: Invalid downcasting causes ClassCastException at runtime.

### 9. serialVersionUID

In object serialization, what is serialVersionUID?

A. A unique identifier for each class version  
B. A method used for serialization  
C. A variable that holds serialized data  
D. A marker interface  

Answer: A  
Explanation: serialVersionUID is used during deserialization to verify class compatibility.

### 10. Marker Interface

What is the purpose of a marker interface in Java?

A. To provide methods for implementation  
B. To mark a class for specific behavior  
C. To prevent multiple inheritance  
D. To enforce type safety  

Answer: B  
Explanation: Marker interfaces have no methods. They mark classes for special behavior.

### 11. static Members

Which statement about static members is true?

A. Static members are associated with the instance of a class  
B. Static members can be accessed without creating an instance of a class  
C. Static members cannot be inherited  
D. Static members can only be private  

Answer: B  
Explanation: Static members belong to the class, not an individual object.

### 12. Blank Final Variable

What is the output?

```java
class Test {
    public final int a;
}

class Example {
    public static void main(String args[]) {
        Test obj = new Test();
        System.out.println(obj.a);
    }
}
```

A. 0  
B. Garbage value  
C. Compile time error: variable is not initialized  
D. Run time error: a is the blank variable  

Answer: C  
Explanation: a is a blank final variable and must be initialized.

### 13. Method Or Constructor

What is the output?

```java
class Example {
    private int x;

    public static void main(String args[]) {
        Example obj = new Example();
    }

    public void Example(int x) {
        System.out.println(x);
    }
}
```

A. 0  
B. Garbage value  
C. Compile time error  
D. No output / blank screen  

Answer: D  
Explanation: public void Example(int x) is a normal method, not a constructor.

### 14. Constructor Selection

What is the output?

```java
class Example {
    private int x;

    public static void main(String args[]) {
        Example obj = new Example(5);
    }

    public Example(int x) {
        System.out.println("x = " + x);
    }

    public void Example(int x) {
        System.out.println(x);
    }
}
```

A. x = 5  
B. 5  
C. Compile time error: ambiguous call of Example(int)  
D. Run time error  

Answer: A  
Explanation: public Example(int x) is the constructor. The void version is a normal method.

### 15. String Pool And equals()

What is the output?

```java
class Test {
    public static void main(String args[]) {
        String str1 = new String("Hello World");
        String str2 = new String("Hello World");

        String str3 = "Hello World";
        String str4 = "Hello World";

        int a = 0, b = 0, c = 0;

        if (str3 == str4)
            a = 1;
        else
            a = 2;

        if (str1.equals(str3))
            b = 1;
        else
            b = 2;

        if (str1 == str4)
            c = 1;
        else
            c = 2;

        System.out.println("a= " + a + " b= " + b + " c= " + c);
    }
}
```

A. a=2 b=1 c=2  
B. a=2 b=2 c=2  
C. a=1 b=2 c=1  
D. a=1 b=1 c=2  

Answer: D  
Explanation: str3 and str4 point to the same string pool object. equals compares content. str1 and str4 are different references.

### 16. String Object Count

How many String objects are created in the above example?

A. 1  
B. 2  
C. 3  
D. 4  

Answer: C  
Explanation: One string pool literal plus two new String objects.

### 17A. HashMap

What is the output?

```java
import java.util.HashMap;
import java.util.Map;

public class MyClass {
    public static void main(String args[]) {
        Map<String, String> hashMap = new HashMap<String, String>();
        hashMap.put(new String("a"), "audi");
        hashMap.put(new String("a"), "ferrari");
        System.out.println(hashMap);
    }
}
```

A. {a=audi}  
B. {a=ferrari}  
C. {a=audi, a=ferrari}  
D. Compile-time error  

Answer: B  
Explanation: HashMap compares keys using equals() and hashCode(), so the second value replaces the first.

### 17B. IdentityHashMap

What is the output?

```java
import java.util.IdentityHashMap;
import java.util.Map;

public class MyClass {
    public static void main(String args[]) {
        Map<String, String> identityHashMap = new IdentityHashMap<String, String>();
        identityHashMap.put(new String("a"), "audi");
        identityHashMap.put(new String("a"), "ferrari");
        System.out.println(identityHashMap);
    }
}
```

A. {a=ferrari}  
B. {a=audi}  
C. Both entries remain, such as {a=audi, a=ferrari}; order may vary  
D. Runtime exception  

Answer: C  
Explanation: IdentityHashMap compares keys using ==, not equals(), so both new String objects are treated as different keys.
