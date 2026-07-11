class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        li=[]
        for i in range(left,right+1):
            oo=True
            for j in str(i):
                if j=="0"or i%int(j)!=0:
                    oo=False
            if oo:
                li.append(i)
        return li
