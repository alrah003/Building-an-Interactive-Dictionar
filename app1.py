import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(w):  
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn= input ("did you mean %s instead Enter Y or N: /n" %get_close_matches(w,data.keys())[0])
        if yn =="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N" :
            return "the word doesn't exist. please double check it"    
        else:
            return " we didn't understand your entry"
    else:
        return "the word doesn't exist. please double check.   "
    return data[w]

word=input ("enter word:")

output= translate(word)

if type(output)==list:
    for item in output:
        print (item)

else:
    print (output)

print (translate (word))





