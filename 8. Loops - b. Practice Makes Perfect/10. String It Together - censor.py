def censor(text,word):
    return text.replace(word, "*" * len(word))
    
print censor("I really like cursing!", "cursing")
