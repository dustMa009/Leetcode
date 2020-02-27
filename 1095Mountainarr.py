class mountarr(object):
    def __init__(self,array):
        self.arr=array
        self.length=len(array)

    def get(self,index):
        return self.arr[index]

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        nnn=mountain_arr.length
        return self.mount(target, mountain_arr,0,nnn-1)
    
    def mount(self,target,mountain_arr,left,right):
        if left>right:
            return -1
        n=mountain_arr.get(left)
        if n==target:
            return left
        if left==right:
            return -1
        if right-left==1:
            if mountain_arr.get(right)==target:
                return right
            else:
                return -1
            
        mid=int((left+right)/2)
        m1=mountain_arr.get(mid)
        if m1>target:
            mm1=self.mount(target,mountain_arr,left+1,mid-1)
            mm2=self.mount(target,mountain_arr,mid+1,right)
            if mm1!=-1:
                return mm1
            elif mm2!=-1:
                return mm2
            else:
                return -1
        m2=mountain_arr.get(mid+1)
        
        if m1<target:
            if m2<m1:
                self.mount(target,mountain_arr,left+1,mid-1)
            if m2>m1:
                if m2>target:
                    return self.mount(target,mountain_arr,mid+2,right)
                elif m2==target:
                    return mid+1
                else:
                    self.mount(target,mountain_arr,mid+2,right)
        else:
            if m2>m1:
                return mid
            else:
                a3=self.mount(target,mountain_arr,left+1,mid-1)
                if a3==-1:
                    return mid
                else:
                    return a3
