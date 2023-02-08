def is_anagram(word):
    frequency  = {}
    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency 

print("Insira a primeira palavra:")
a_word = input()
print(" ")
print("Insira a segunda palavra:")
b_word = input()
print(" ")

if (len(a_word) != len(b_word)):
   print ("False")
else:
    if (is_anagram(a_word) == is_anagram(b_word)):
        print("True")
    else:
        print("False")