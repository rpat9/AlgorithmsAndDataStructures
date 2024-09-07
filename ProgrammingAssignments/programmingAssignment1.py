'''

P-1.36: Write a Python program that inputs a list of words, separated by whitespace , and outputs how many times each word appears in the list. 
You dont need to worry about efficiency at this point, however, as this topic is something that will be addressed later in this book.

'''

def count_words(words):
    word_count = {}

    listOfWords = words.split()

    for word in listOfWords:
        if word in word_count:  # Adds 1 if the word already exists.
            word_count[word]+=1
        else:
            word_count[word] = 1   # Makes a new entry in dict if a new word appears

    return word_count
 
if __name__ == '__main__':
 
    words = "abc ab mno abc a vwx vwx stu mno abc"
    words2 = "abc abc abc"
    print(count_words(words)) # {'abc': 3, 'vwx': 2, 'a': 1, 'mno': 2, 'ab': 1, 'stu': 1}
    print(count_words(words2)) # {'abc': 3}