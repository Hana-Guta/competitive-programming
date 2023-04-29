class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        ans=''
        for ch in s:
            if ch=='(':
                stack.append(ans)
                ans=''
            elif ch==')':
                prev=stack.pop()
                ans=ans[::-1]
                ans=prev+ans
            else:
                ans+=ch
        return ans
