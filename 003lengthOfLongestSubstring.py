class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        else:
            submax=1
            sub=s[0]
            for i in range(1,len(s)):
                if s[i] in sub:
                    b=sub.index(s[i])+1
                    submax=max(submax,len(sub))
                    sub=sub+s[i]
                    sub=sub[b:]
                else:
                    sub=sub+s[i]

            submax=max(submax,len(sub))
            return submax
