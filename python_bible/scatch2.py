# get sentence from user
original = input("Enter in a sentence").strip().lower()
#split sentence into words
words = original.split()
print(words)
#loop through words and convert to pig latin
new_words = []
#if starts with vowel, just add "yay"
for word in words:
 if word[0] in [aeiou]:
     new_word == word + "yay"
     new_words.append(new_word)
     print(new_words)
 
#Otherwise, move the first consonant cluser to end, and add "ay"
#stick words back together
" ".join(new_words)|
#output the final string
