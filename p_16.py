''' Write a Python program to count the occurrences of each word in a 
given sentence'''
def count_word_occurrences(sentence):
    words = sentence.lower().split()
    
    word_counts = {}
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts
sentence = "This is a test sentence. This test is only a test."
word_counts = count_word_occurrences(sentence)
print(word_counts)
