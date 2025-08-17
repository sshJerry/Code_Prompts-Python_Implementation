/*
Given an array of strings strs,
group the anagrams together.
You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]



Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

 */

/*
Can the array of str be empty or null? No
How big is the array of strs? Not too big but what's always atleast one element passed in
Does the array of strs have non english lowercase characters? Consists of only lowercase english letters
Will we receive duplicate?
 */

import java.util.*;
import java.util.stream.Collectors;

/*
We have to Hash the input reliably and use that as a key to compare. The easiest way to compare is
through sorting the string and using that as a key to compare against other strings. Through the use
of a Hashmap we will maintain a List<String> tied to that key. That list will be composed of all anagrams
to the sorted key. After one pass, return the values of the HashMap as a List of a List<String>

Original thought to use the isAnagram function from LC 242 Valid Anagram but deemed it too inefficient

Space complexity of the groupAnagrams method is O(n) as we have to iterate and store a value for every
iteration until input.length().

Space complexity of the sortString method is k+K = O(k) as we use space to create an array of chars
the same length as the string. We then wrap the sorted array in a return to value thats useful.

Within every iteration of a string, we call a function that iterates through the entire string,

SC O(N * K) = O(N)

Time Complexity of the groupAnagrams method is O(N) as hashmap operations happen in O(1) time but we
iterate every n.

Time complexity of the sortString method depend on the algorithm behind Arrays.sort().
At its worse, this is a O(N Log N) TC.

 */
public class LC49GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> sortedStringToGroupedAnagrams = new HashMap<>();
        for (String str : strs) {
            String sortedString = sortString(str);
            List<String> listOfAnagrams = sortedStringToGroupedAnagrams.getOrDefault(sortedString, new ArrayList<>());
            listOfAnagrams.add(str);
            sortedStringToGroupedAnagrams.put(sortedString, listOfAnagrams);
        }
        return new ArrayList<>(sortedStringToGroupedAnagrams.values());
    }

    public String sortString(String unsortedString) {
        char[] charArray = unsortedString.toCharArray();
        Arrays.sort(charArray);
        return new String(charArray);
    }
}
