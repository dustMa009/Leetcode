def comp(str1,str2):
    if str1=='' or str2=='' :
        return ''
    else:
        k=0
        for i in range(min(len(str1),len(str2))):
            if str1[i]==str2[i]:
                k=k+1
            else:
                break

        return str1[0:k]


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ''
        else:
            c=strs[0]
            for each in strs:
                c=comp(each,c)
                if c=='':
                    break

            return c

    
