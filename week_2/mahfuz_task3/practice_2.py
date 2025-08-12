# Task 2
# 6
name = "I love learnig python"
print("python" in name)


# 7
word = "enjoyment"
print("".join(reversed(word)))

#8
name = "    program     "
print(name.strip())

#9
word = input("Please enter a sentence: ")
vowel_o = word.lower().count("o")
vowel_i = word.lower().count("i")
vowel_u = word.lower().count("u")
vowel_e = word.lower().count("e")
vowel_a = word.lower().count("a")
total = vowel_o + vowel_i + vowel_u + vowel_e + vowel_a
print(total)

# 10
name = "1234"
text_new = int(name)
text_final = text_new * 2
print(text_final)
