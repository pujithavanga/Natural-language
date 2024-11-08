import nltk
nltk.download('averaged_perceptron_tagger')
training_data = [
    [('The', 'DT'), ('cat', 'NN'), ('is', 'VBZ'), ('on', 'IN'), ('the', 'DT'), ('mat', 'NN')],
    [('I', 'PRP'), ('love', 'VBP'), ('eating', 'VBG'), ('pizza', 'NN')]
]
rules = [
    ('NN', 'VBZ', 'VBG'),  
    ('NN', 'VBZ', 'NN'),  
    ('VBG', 'NN', 'VBG'), 
]
for sentence in training_data:
    for i in range(len(sentence) - 1):
        for (tag1, tag2, new_tag) in rules:
            if (sentence[i][1] == tag1 and sentence[i+1][1] == tag2):
                sentence[i] = (sentence[i][0], new_tag)
test_sentence = "The cat is on the mat"
tagged_sentence = nltk.pos_tag(test_sentence.split())
print("Original test sentence:", test_sentence)
print("Tagged sentence after transformation:", tagged_sentence)
