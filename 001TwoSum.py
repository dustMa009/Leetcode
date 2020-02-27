class solution(object):
    def twosum(self,nums,target):
        index1=0
        for each in nums:
            nums[index1]=0.5
            if target-each in nums:
                index2=nums.index(target-each)
                break
            else:
                nums[index1]=each
                index1=index1+1   
        return([index1,index2])
    
