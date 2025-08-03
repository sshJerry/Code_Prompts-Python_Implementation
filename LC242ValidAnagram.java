import java.util.HashMap;
import java.util.Map;

/***
 *Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 *
 * Example 1:
 * Input: s = "anagram", t = "nagaram"
 * Output: true
 *
 * Example 2:
 * Input: s = "rat", t = "car"
 * Output: false

 * Constraints:
 * 1 <= s.length, t.length <= 5 * 104
 * s and t consist of lowercase English letters.

 * Follow up: What if the inputs contain Unicode characters?
 * How would you adapt your solution to such a case?
 */
public class LC242ValidAnagram {
    public boolean isAnagram(String s, String t) {
        //INPUT
        // Two Strings of AT LEAST length n = 1 and at most a large string
        // OUTPUT
        // TRUE or FALSE

        // TEST CASES
        // s = "abcd" t = "cdab" => True
        // s = "Github" t = "Google" => False

        // First check if s == t and return true
        // Second check if s.length() != t,length() and return false

        /***
         * What I'm thinking is iterating through the first string (s) and at every character,
         * evaluating that character against string t using Strings replaceFirst() or StringBuilders deleteCharAt().
         * If by the time we reach end of string s and there's still remaining characters in String t
         * , then it is NOT an anagram
         *
         * Problem: O(n^2) time and performance overhead with shifting operations
         *
         * Frequency Counting using HashMaps?
         */

        // Hashmap of String Character to Integer Count
        // Iterate over first word incrementing with every non unique character
        // Then iterate over second word, decrementing if exists and if it doesn't exist return false
        // If we get to the end then return true
        if (s.equals(t))
            return true;
        if (s.length() != t.length())
            return false;

        Map<Character, Integer> characterCounter = new HashMap<>();
        for (Character c : s.toCharArray()){
            if (null == characterCounter.get(c) || characterCounter.get(c) == 0){
                characterCounter.put(c, 1);
                continue;
            }
            characterCounter.put(c, characterCounter.get(c) + 1);
        }
        System.out.println(characterCounter.entrySet());
        for (Character c : t.toCharArray()){
            if (characterCounter.get(c) == null || characterCounter.get(c) == 0)
                return false;
            characterCounter.put(c, characterCounter.get(c) - 1);
        }
        System.out.println(characterCounter.entrySet());
        return true;
    }
}

/***
 * Notes: O(n * m) so O(n). Improvement that can be made is using getOrDefault in the future.
 */
