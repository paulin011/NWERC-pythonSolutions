class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs==1):
            return strs[0]
        s = strs[0][0:1]
        for word in strs:
            if s != word[0:1]:
                return ""
        for i in range(1,len(strs[0])):
            s = strs[0][0:i+1]
            for word in strs:
                if s != word[0:i+1]:
                    return s[0:i]
        return ""
    def main():
        string = [""]
        print(longestCommonPrefix(string))
