def isValid( s: str) -> bool:
        r,e,g = [],[],[]
        for i in range(len(s)):
            if s[i] == "(":
                r.append(i)
            elif s[i] == "[":
                e.append(i)
            elif s[i] == "{":
                g.append(i)


            elif s[i] == ")":
                if len(r) == 0:
                    return False
                elif len(e) != 0:
                    if r[-1] < e[-1]:
                        return False
                elif len(g) != 0:
                    if r[-1] < g[-1]:
                        return False
                r.pop(-1)
            elif s[i] == "]":
                if len(e) == 0:
                    return False
                elif len(r) != 0:
                    if e[-1] < r[-1]:
                        return False
                elif len(g) != 0:
                    if e[-1] < g[-1]:
                        return False
                e.pop(-1)            
            elif s[i] == "}":
                if len(g) == 0:
                    return False
                elif len(e) != 0:
                    if g[-1] < e[-1]:
                        return False
                elif len(r) != 0:
                    if g[-1] < r[-1]:
                        return False
                g.pop(-1)
        return len(r)==0 and len(e)==0 and len(g) ==0
    
def main():
        s="()[]{}"
        print(isValid(s))
        s1 = "([])"
        print(isValid(s1))
        s2 = "([([)]])"
        print(isValid(s2))

main()