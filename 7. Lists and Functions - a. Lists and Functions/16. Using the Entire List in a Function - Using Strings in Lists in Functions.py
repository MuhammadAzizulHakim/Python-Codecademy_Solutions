n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for n in range(len(words)):
       result += words[n]
    return result

print join_strings(n)
