/*
Given two strings s and t,
return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters?
How would you adapt your solution to such a case?
 */

/*
How big in terms of length can we expect for these characters? Pretty Big
Can these Strings be null or length 0? No
Can these Strings be only whitespace? No

Two words are Anagrams if the characters that make up the word can be used to make another word.
 */

/*
A brute force method would be to iterate through s and remove a character in s and t until both their
lengths are zero. If we iterate through s and there's still a length on t or t is of length 0, then
its an anagram.

A better solution would be utilizing HashMaps

Hashmap<Character, Integer>
Adding to the Hashmap is o(1), checking o(1)
Example 2:
Input: s = "rat", t = "car"

for Character : s
    If(Hashmap.containsKey(Character))
        hashMap.put(Character, hashMap.get()+1)
    hashMap.put(Character, hashMap.get()+1)

for Character : t
    if (hashMap.containsKey(Character) && hashMap.get(Character) != 0)
        hashMap.put (Character, hashMap.get(Character)-1)
     return false;
return true;
 */

import java.util.HashMap;
import java.util.Map;

public class LC242ValidAnagram1 {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> characterToCountMap = new HashMap<>();

        if (s.length() != t.length())
            return false;
        for(Character sChar : s.toCharArray()) {
            characterToCountMap.put(sChar, characterToCountMap.getOrDefault(sChar, 0) +1);
        }

        for(Character tChar : t.toCharArray()) {
            if (characterToCountMap.containsKey(tChar) && characterToCountMap.get(tChar) >0){
                characterToCountMap.put(tChar, characterToCountMap.get(tChar)-1);
                continue;
            }
            return false;
        }
        return true;
    }
}
