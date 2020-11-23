str1 = "just a totally normal sentence"
spaced_str1 = ""

for i in range(len(str1)):
    character = str1[i] 
    spaced_char = character + " "
    spaced_str1 = spaced_str1 + spaced_char
    
print(spaced_str1)