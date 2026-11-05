t = "abdbh"
s = "a"

def isSubsequence(s, t):
    count = 0
    if len(s) != 0 and count < len(s):
        for i in t:
            if count < len(s):
                if s[count] == i:
                    count += 1
    else:
        return True

    
        
    if count == len(s):
        return True
    else:
        return False

print(isSubsequence(s,t))