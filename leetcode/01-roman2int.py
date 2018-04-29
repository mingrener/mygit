class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lib_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ret = 0
        pre_int = 0
        for i in range(len(s)):
            cur_int = lib_dict[s[i]]
            ret += cur_int
            if cur_int > pre_int:
                ret -= pre_int*2
            pre_int = cur_int
        return ret
if __name__=="__main__":
    su = Solution()
    ret = su.romanToInt("MCMXCIV")
    print(ret)