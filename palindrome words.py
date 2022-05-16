def palindrome(sentence):
    for i in (",.'?/><}{{}}'"):
        sentences = sentence.replace(i, "")
        palindrome = []
        words = sentence.split(' ')
        for word in words:
            word = word.lower()
            if word == word[::-1]:
                palindrome.append(word)
        return palindrome
sentence = input("Enter a sentence : ")
print(palindrome(sentence))