import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
 */
public class LC20ValidParentheses {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> bracketMap = new HashMap<>();
        bracketMap.put('}', '{');
        bracketMap.put(')', '(');
        bracketMap.put(']', '[');

        if (s.length() <= 1){
            return false;
        }
        for (Character c : s.toCharArray()) {
            if (c == '{' || c == '[' || c == '(') {
                stack.push(c);
            }
            if (c == '}' || c == ']' || c == ')') {
                if (!stack.empty() && stack.peek() == bracketMap.get(c)) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        return stack.empty();
    }
}
