class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        smallest=strs[0]
        for i in range(1,len(strs)):
            if len(strs[i])<len(smallest):
                smallest=strs[i]
        ans=""
        boo=True
        for i in range(len(smallest)):
            prefix=smallest[:i+1]
            for j in range(len(strs)):
                if prefix not in strs[j][:i+1]:
                    boo=False
                    break
            if boo:
                ans=prefix
        return ans
