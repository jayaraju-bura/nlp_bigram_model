def read_corpus():
    data = ['This is a  dog','This is a cat','I love my cat','This is my name ']
    words = []
    for i in range(len(data)):
        for word in data[i].split():
            words.append(word)
    
    print(words)
    return words
    
def create_bigrams_from_tokenized_words(words):
    list_of_bigrams = []
    bigram_counter = {}
    unigram_counter = {}
    for idx in range(len(words)-1):
        if idx < len(words) - 1 and words[idx+1].lower():
            list_of_bigrams.append((words[idx], words[idx+1]))
            
            if (words[idx], words[idx+1]) in bigram_counter:
                bigram_counter[(words[idx], words[idx+1])] += 1
            else:
                bigram_counter[(words[idx], words[idx+1])] = 1
                
            if words[idx] in unigram_counter:
                unigram_counter[words[idx]] += 1 
            else:
                unigram_counter[words[idx]] = 1
                
    return list_of_bigrams, bigram_counter, unigram_counter
    
def calculate_bigram_prob(list_of_bigrams, bigram_counter, unigram_counter):
    bigrams_prob_map = {}
    for bigram in list_of_bigrams:
        word_one = bigram[0]
        word_two = bigram[1]
        bigrams_prob_map[bigram] = bigram_counter.get(bigram)/unigram_counter.get(word_one)
    
    return bigrams_prob_map
        
    
        

if __name__ == '__main__':
    tokenized_words = read_corpus()
    list_of_bigrams, bigram_counter, unigram_counter = create_bigrams_from_tokenized_words(tokenized_words)
    
    
    print("\n printing the list of bigrams")
    print(list_of_bigrams)
    
    print("\n print the frequncies of unigrams in the corpus")
    print(unigram_counter)
    
    print("\n print the frequencies of bigrams in the corpus")
    print(bigram_counter)
    
    bigrams_prob_map = calculate_bigram_prob(list_of_bigrams, bigram_counter, unigram_counter)
    print("\n Printing the probabities of bigrams:: ")
    print(bigrams_prob_map)
    
    input_string = "This  is my cat"
    input_data = input_string.split()
    
    test_bigram_list = []
    for idx in range(len(input_data)-1):
        if idx < len(input_data) - 1:
            test_bigram_list.append((input_data[idx], input_data[idx+1]))
            
    final_prob = 1 
    
    for bigram in test_bigram_list:
        if bigram in bigrams_prob_map:
            final_prob *= bigrams_prob_map[bigram]
        else:
            for key in bigram_counter.keys():
                bigram_counter[key] += 1
            for key in unigram_counter.keys():
                unigram_counter[key] += 1
            if bigram not in bigram_counter:
                bigram_counter[bigram] = 1 
            if bigram[0] not in unigram_counter:
                unigram_counter[bigram[0]] = 1  
            list_of_bigrams.append(bigram)
            bigrams_prob_map = calculate_bigram_prob(list_of_bigrams, bigram_counter, unigram_counter)
            print("\n",bigrams_prob_map)
            final_prob *= bigrams_prob_map[bigram]
     
    print("\n The probability of the sentence [This is our cat] in the corpus is :::: " + str(final_prob))



# ['This', 'is', 'a', 'dog', 'This', 'is', 'a', 'cat', 'I', 'love', 'my', 'cat', 'This', 'is', 'my', 'name']

#  printing the list of bigrams
# [('This', 'is'), ('is', 'a'), ('a', 'dog'), ('dog', 'This'), ('This', 'is'), ('is', 'a'), ('a', 'cat'), ('cat', 'I'), ('I', 'love'), ('love', 'my'), ('my', 'cat'), ('cat', 'This'), ('This', 'is'), ('is', 'my'), ('my', 'name')]

#  print the frequncies of unigrams in the corpus
# {'This': 3, 'is': 3, 'a': 2, 'dog': 1, 'cat': 2, 'I': 1, 'love': 1, 'my': 2}

#  print the frequencies of bigrams in the corpus
# {('This', 'is'): 3, ('is', 'a'): 2, ('a', 'dog'): 1, ('dog', 'This'): 1, ('a', 'cat'): 1, ('cat', 'I'): 1, ('I', 'love'): 1, ('love', 'my'): 1, ('my', 'cat'): 1, ('cat', 'This'): 1, ('is', 'my'): 1, ('my', 'name'): 1}

#  Printing the probabities of bigrams:: 
# {('This', 'is'): 1.0, ('is', 'a'): 0.6666666666666666, ('a', 'dog'): 0.5, ('dog', 'This'): 1.0, ('a', 'cat'): 0.5, ('cat', 'I'): 0.5, ('I', 'love'): 1.0, ('love', 'my'): 1.0, ('my', 'cat'): 0.5, ('cat', 'This'): 0.5, ('is', 'my'): 0.3333333333333333, ('my', 'name'): 0.5}

#  The probability of the sentence [This is our cat] in the corpus is :::: 0.16666666666666666
