def popularity(text):
    print(f"In:{text}")
    wordPop = dict()
    words = text.lower().split(" ")
    words.sort()
    wordPop = dict.fromkeys(words, 0)
    
    for element in words:
        wordPop.update({element: wordPop[element]+1}) 

    wordPop = sorted(wordPop, key = wordPop.get, reverse=True)
            
    return wordPop



print(f"Out: {popularity('apple kiwi pineapple kiwi apple kiwi')}\n")
print(f"Out: {popularity('aPPle pine aApple kiwi Apple kiwi')}\n")
print(f"Out: {popularity('aPPle pine Apple kiwi Apple kiwi')}\n")
print(f"Out: {popularity('aab aaa aac aab aac aaa x')}\n")