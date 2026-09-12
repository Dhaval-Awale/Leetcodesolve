class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Create a stack to store the open brackets
        stack = []
        
        # Use a dictionary to store the mappings between open and close brackets
        bracket_map = {'(': ')', '[': ']', '{': '}'}
        
        # Iterate through the string
        for c in s:
            # If the character is an open bracket, push it onto the stack
            if c in bracket_map:
                stack.append(c)
            # If the character is a close bracket, check if it is the corresponding closing bracket for the top element of the stack
            elif not stack or bracket_map[stack.pop()] != c:
                return False
        
        # If the stack is empty at the end, then the string is valid
        return not stack