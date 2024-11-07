import random
text = "The man makes profit with the use of poultry farming"
words = text.split()
bigrams = {}
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word in bigrams:
        bigrams[current_word].append(next_word)
    else:
        bigrams[current_word] = [next_word]
current_word = "man"
generated_text = current_word
length = 20
for _ in range(length - 1):
    if current_word in bigrams:
        next_word = random.choice(bigrams[current_word])
        generated_text += ' ' + next_word
        current_word = next_word
    else:
        break
print(generated_text)
