class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch!="*":
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    continue
        return "".join(stack)
        