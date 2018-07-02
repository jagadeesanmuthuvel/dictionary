import json
import difflib
from difflib import get_close_matches
data = json.load(open("data.json", "r"))

word = input("enter the word:")
def worddic(word):
    word=word.lower()
    if  word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn=input("Did u mean %s? y or n" % get_close_matches(word, data.keys())[0])
        if yn is "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn is "n":
            return "check it"

    else:
        return "not exist"
out = worddic(word)
if type(out) == list:
    for item in out:
        print(item)
else:
     print(out)
