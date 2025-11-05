def isBalanced(s):
    #* Khoi tao stack
    st = []
    
    for c in s:
        #* Neu la dau "(" , "[" , "{" thi them vao stack
        if (c == "(" or c == "[" or c == "{"):
            st.append(c)
            
        #* Neu la cac dau dong ngoac
        #* TH1: kiem tra neu stack rong (dau dong ngoac o dau day)
        #* TH2: chua co dau mo ngoac tuong ung
        elif (c == ")" or c == "]" or c == "}"):
            if not st: return False
            top = st[-1]
            
            if ((c == ")" and top != "(") or 
                (c == "]" and top != "[") or 
                (c == "}" and top != "}")):
                return False
            
            st.pop()
    
    #* Kiem tra neu stack rong (phong truong hop con thua dau dong ngoac)
    return not st

s = "[()()]{}"
print("true" if isBalanced(s) else "false")