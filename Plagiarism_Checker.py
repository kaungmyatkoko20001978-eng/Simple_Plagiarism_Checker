def plagiarism_check(filename1, filename2):
    import re # I tried to use regex module for cleaning the text
    with open(filename1, 'r') as f:
        text = f.read()
        text1 = text.lower() #To even out the text and avoid deleting capital letters by accident later on
        content1 = re.sub(r"[^a-z\s]", "", text1) #cleaning everything except white spaces and lower case characters
        content1 = re.sub(r"\s+", " ", content1).strip() #removing outer white spaces 
    with open(filename2, 'r') as f:
        txt = f.read()
        txt1 = txt.lower()
        content2 = re.sub(r"[^a-z\s]", "", txt1) 
        content2 = re.sub(r"\s+", " ", content2).strip()
    #The following list of words are gotten from ntlk documentation.
    support_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
              'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    rcontent1 = list(content1.split(' ')) #listing the words in the entire file to count freq with dictionaries later on
    rcontent2 = list(content2.split(' ')) # same thing here...
    filtered_1 = [word for word in rcontent1 if word not in support_words] #removing supporting/stop words to improve accuracy and miscalculation
    filtered_2 = [word for word in rcontent2 if word not in support_words] #same thing here, I tried list comprehension for cleaner code

    set1 = set(filtered_1) #removing duplicates for jaccard calculation
    set2 = set(filtered_2) #jaccard method checks word freq level only, it only look at the number of time each word appears and compare them for plagiarism
    common = set1 & set2   #so...it won't be as accurate as n-gram
    total = set1 | set2
    similar=len(common) / len(total)
    print(f"Jaccard Similarity Rate: {similar:.2%}") #string modifier .2% means to show the percentage up to 2 decimal points
    def get_ngrams(words, n=4):
        return set(tuple(words[i:i+n]) for i in range(len(words) - n + 1)) # a function that returns n-grams without ruining order of words
    n = 4
    grams1 = get_ngrams(filtered_1, n)
    grams2 = get_ngrams(filtered_2, n)
    similarity = len(grams1 & grams2) / len(grams1 | grams2)
    print(f"Plagiarism Rate Through Phrase Detection (using {n}-word phrases via n-grams: {similarity:.2%}")

if __name__ == '__main__':
    plagiarism_check(filename1='michelle_obama_speech.txt', filename2='melania_trump_speech.txt') #testing
