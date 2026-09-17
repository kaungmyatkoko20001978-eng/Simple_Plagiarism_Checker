#You will need to install spacy first, type this into your terminal:
#pip install spacy
#btw Ubuntu is better than Windows...pls don't get mad...jk both have their own purposes
#I became a VERY VERY lazy programmer so...yeah...I just hopped onto the library 

def check_plagiarism(filename1, filename2):
    import spacy
    with open(filename1, 'r') as f: #opening...reading files...just some boring stuff
          text1 = f.read()
    with open(filename2, 'r') as f:
          text2 = f.read()
    process = spacy.load("en_core_web_sm") #I loaded the language model here :D
    s1=process(text1) #putting the file into the process object
    s2=process(text2) #same here
    percent=s1.similarity(s2)
    print(f"Percentage: {percent:.2%}")
