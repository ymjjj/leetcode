class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = s.lower()
        
        length = len(s)
        str = []
        for i in range(length) :
            if 'a'<=ns[i]<='z' or '0'<=ns[i]<='9':
                str.append(ns[i])
        if len(str) == 0 :
            return True
        lp = 0
        rp = len(str) - 1
        while lp < rp :
            if str[rp] == str[lp] :
                lp += 1
                rp -= 1
            else :
                return False
        return True
solution = Solution()
s = "A man, a plan, a canal: Panama"
a = solution.isPalindrome(s)
print(a)