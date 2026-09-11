# Simple_Plagiarism_Checker
Used Jaccard and n-gram similarity to check the percentage of copied work between two text files.

Jaccard Similarity: I used this for word level checking. In plagiarised writings, words between the copied and the original are mostly same. This is useful for checking how common the words between two writings overlap.
Formula => J(A, B) = n(A intersect B)/ n(A union B)

For those who want to know how n-grams work:
An n-gram is a sequence of items (for example: letters, words, or blocks of text and speech).
N = number of elements per item.
N-grams are very useful for: Predicting text (by guessing the next word as we type messages; can be seen on Gboard as an example)
                             Spelling check and grammar check (finding some words in a phrase or finding a phrase in a block of text that
                             seems out of place or wrong in terms of logic.

#How the function works:
 def get_ngrams(words, n=3):
        return set(tuple(words[i:i+n]) for i in range(len(words) - n + 1))
Take a good look at this function that I made. Let me explain how it works. Firstly, we need to know how many loops to make and up to which place. Since we want to loop until the list doesn't have enough logical position to make tuples consisting of 3 items. What does that mean? That means we have to loop until the index of the list has 2 positions left. To know until which index to loop, we subtract the (n) number. We must add 1 because the range function stops before the last or limited number.

If the explanation was a bit confusing...let me show you visually.


For the visual learners:

5_words = [a, b, c, d, e]
           |  |  |
         valid starts

For n = 3, you can start at 0, 1, 2 -- the last 2 can't start a 3-word phrase.
So, the three possible slices with correct order: ('a', 'b', 'c'), ('b', 'c', 'd'), and ('c', 'd', 'e')

5 words, n = 3 -> starts 0, 1, 2 -> range(3) -> range(5-3+1)

    set(  tuple(words[i:i+n])  for i in range(len(words) - n + 1)  )
    |---------------------|      |---------------------------------|
            │                           │
       What to create           What to loop over and until what index

Here, --words[i:i+n]-- slices the list. i increases because of the range function every time to move the index to the next position next to it by 1. So....i + 1 every time it loops due to range(). +n is for the number of elements we take per slice.

Why did you use sets? -- I am pretty sure you may wonder that. The use of sets is important because we want to find the phrases that overlap between both text files. In math, we call that overlap the intersection; to find the intersection easily, we use sets.
