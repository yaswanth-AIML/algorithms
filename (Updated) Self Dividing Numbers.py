class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        li=[]
        for i in range(left,right+1):
            oo=True
            temp=i
            while temp>0:
                do=temp%10
                if do==0 or i%do!=0:
                    oo=False
                temp=temp//10
            if oo:
                li.append(i)
        return li
