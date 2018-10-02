code = "asd; \" \
/* \
asdasdasdasd \
asdasd tttttt \
*/ \""
in_comment = False
in_multiline = False
in_quote = False
wait_symbol = False
skip = True
c = 0

for y in code:
    if y == '"' and not in_comment and not in_multiline:
        in_quote = not in_quote
        
    if wait_symbol:
        if y == "/":
            if in_multiline:
                in_multiline = False
            else:
                in_comment = True
        elif y == "*":
            in_multiline = True
        
    if (in_multiline and y == "*" or y == "/") and not wait_symbol and not in_quote:
        wait_symbol = True
        
    if y == "\n" and in_comment:
        in_comment = False
        
    if in_comment or in_multiline:
        if y == " " or y == "\n":
            skip = False
            c = 0
        elif skip:
            c = 0
        
        elif y != "tttttt"[c]:
            skip = True
        elif c < 5:
            c+=1
        else :
            print("FIND")
