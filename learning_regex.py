import re

# lesson 1
# returns all the occurences of the string searched for in the expression

text = "On the horizon"
x = re.findall("on", text.lower())
print(x)

# lesson 2
# this returns the position of the string in the expression

text = "python is quite an interesting programming language"
x = re.search('interesting', text)
print(x.start(), "----", x.end())

# lesson 3
# this returns a list with the string that occurs in the expression being eliminated
# it does the same job with the traditional "split" method
text = "I hate the smell of goats"
x = re.split("goats", text)
print(x)

# lesson 4
# this checks if the text is found in the beginning of the expression
text = "python is quite an interesting programming language"
x = re.findall("^python", text)
if x:
    print("our expression starts with the word python")
    
# lesson 5    
# this checks a string for a pattern that matches digits in the format below and returns the first result
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number 415-555-4342 is 415-555-4242.')
print("the first occurence of our search is ", mo.group())

    
    
