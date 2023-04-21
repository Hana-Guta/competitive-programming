class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for i in range(len(tokens)):
            operator = tokens[i]
            if operator=='+' or operator=='-' or operator=='*' or operator=='/':
                one=int(stack.pop())
                two=int(stack.pop())
                if operator=='+':
                    stack.append(two+one)
                elif operator=='-':
                    stack.append(two-one)
                elif operator=='*':
                    stack.append(two*one)
                else:
                    stack.append(two/one)
            else:
                stack.append(operator)
        return int(stack[0])
