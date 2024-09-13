import functools

class Solution:
    def crackPassword(self, password: List[int]) -> str:
        def cmp(a,b):
            if a+b==b+a:
                return 0
            elif a+b>b+a:
                return 1
            else:
                return -1
        num_s=list(map(str,password))
        num_s.sort(key=functools.cmp_to_key(cmp))
        return ''.join(num_s)