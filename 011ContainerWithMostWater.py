class Solution(object):  #1万长度数组炸了，太慢
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h1,h2=0,0
        area=0
        for i1 in range(len(height)-1):
            if height[i1]<=h1:
                continue
            else:
                h1=height[i1]
                
                half=height[i1+1:][::-1]
                h2=0
                for i2 in  range(len(half)):
                    if half[i2]<=h2:
                        continue
                    else:
                        h2=half[i2]
                        temp=min(height[i1],half[i2])*(len(height)-1-i1-i2)
                        if temp>area:
                            area=temp

        return area
                        
