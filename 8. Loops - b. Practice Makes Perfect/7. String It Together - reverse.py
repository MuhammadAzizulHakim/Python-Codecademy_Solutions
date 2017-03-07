#version1:
def reverse(text):
    rev_text = ""
    letters = len(text)
    while letters > 0:
        rev_text += text[letters - 1]
        letters -= 1
    return rev_text
    
print reverse("kentut")
print reverse("brotbrotbroot")


#version2:
def reverse(text):
    r = list(text)
    r.reverse()
    return "".join(r)
    
print reverse("kentut")
print reverse("brotbrotbroot")
