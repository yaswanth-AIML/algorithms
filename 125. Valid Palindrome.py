class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        right=len(s)-1
        left=0
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False
        return True
