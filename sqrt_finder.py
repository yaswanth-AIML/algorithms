class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        elif x==1 or x==2:
            return 1
        else:
            for i in range(1,x):
                sum=i*i
                if (sum==x):
                    return i
                elif (sum>x):
                    return i-1
