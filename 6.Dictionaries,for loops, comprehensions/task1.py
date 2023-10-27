#Task 1
#Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values.

input_sentence = input("Enter a sentence: ")


word_count = {}

for word in input_sentence.split():   
    word = word.strip('.,!?()[]{}"\'').lower()    
    word_count[word] = word_count.get(word, 0) + 1

print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")

