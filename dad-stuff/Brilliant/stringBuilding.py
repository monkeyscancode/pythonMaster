str1 = "elongate"
spaced_str = ""
for i in range(len(str1)):
    character = str1[i]
    spaced_char = character + character
    spaced_str = spaced_str + spaced_char
print(spaced_str)