#version1:
def anti_vowel(text):
    vowels = ['a','A','e','E','i','I','o','O','u','U']
    NoVowels = ""
    for char in text:
        for vowel in vowels:
            if char == vowel:
                break
        else:
            NoVowels += char

    return NoVowels
    
print anti_vowel("Hey You!")
print anti_vowel('test aiueoAIUEO')


#version2:
def anti_vowel(text):
    return "".join([i for i in text if i.lower() not in 'aiueo'])
    
print anti_vowel("Hey You!")
print anti_vowel('test aiueoAIUEO')


#version3:
def anti_vowel(text):
    
    word = []
    vowel_word = ""
    
    for i in text:
        word.append(i)
        
    for i in range(len(word)):
        for i in word:
            x = word.index(i)
            if i in "aiueoAIUEO":
                word.pop(x)
                
    for i in word:
        vowel_word += "".join(i)
        
    return vowel_word
    
print anti_vowel("Hey You!")
print anti_vowel('test aiueoAIUEO')
