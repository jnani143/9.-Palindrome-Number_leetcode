class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y=str(x)
        l=0
        h=len(str(x))-1
        while l<=h:
            if y[l]==y[h]:
                h-=1
                l+=1
            else:
                return False
        return True
