def strStr( haystack: str, needle: str) -> int:
    i = 0
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

def main():
    a = "abc"
    b = "c"
    print(strStr(a,b))

main()