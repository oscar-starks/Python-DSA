import re

# lesson 1
# returns all the occurences of the string searched for in the expression

text = "On the horizon"
x = re.findall("on the", text.lower())
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
x = re.split("smell", text)
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

# lesson 6
# this divides the search pattern into smaller groups and recieves indexes as arguments with the whole string
# having the index of 0. The "groups()" method returns all the groups at once
regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = regex.search("my number is 123-456-7890")
print(mo.group(2))
print(mo.groups())

# lesson 7
# this matches a string with its possible different occurences using the pipe(|) operator
# and I can check the part that was matched in the group() function
regex = re.compile('Spider(man|woman|girl|chicken)')
searching = regex.search("Spiderman is the king")
print(searching.group(1))

# this section basically checks conditionally. the part of the string inside the brackets is checked only if present
rex = re.compile(r"batsoldier(s)?")
searches = rex.search("that is the batsoldiers we talk about")
print(searches.group())

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

# this section talks about repetition in a pattern e.g banana, bananananana... lol
# '*' simply matches zero or more occurences of that string
regex = re.compile(r"ba(na)*")
results = regex.search("I love banananananananananan")
print(results.group())

# '+' matches one or more occurences of that string in the expression
regex = re.compile(r"ba(na)+")
results = regex.search("I love bananananananananana")
print(results.group())

# you can add the range of numbers of characters you want to match inside curly braces to avoid having to manually match these strings
# {n} matches a repetition of n, {n,} matches repetition of n and above, {,n} matches repetition of 0-n
regex = re.compile(r"ba(na){5,}")
results = regex.search("I love bananananananananana")
print(results.group())

# the findall method basically returns all the occurences of a pattern in a string and not just the first occurence
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('My number 415-555-4342 is 415-555-4242.'))

# this shows how to match a number and more, a white space and a word or collection of characters
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

# this is how you try to find the occurences of characters in a string. this is going to return a list of all the occurences of that character
# remember, it must always be inside the square brackets
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

# this checks if characters within a range are found in your expression
alpharegex = re.compile(r"[A-Z]")
print(alpharegex.findall("this is A TEST"))

# this checks that characters within a range should not be returned in your expression using '^'
alpharegex = re.compile(r"[^A-Z^\s]")
trythis = re.compile(r"[@#$%^&*()_+-=]")
print(trythis.findall("this is A TEST $%^"))
print(alpharegex.findall("this is A TEST $%^"))

# this is used to check if a string starts and ends with numbers by using the "$" sign at the end,
# which signifies that the string should end with that character
digit_search = re.compile(r"^\d+$")
result = digit_search.search("4545678945")
print(result.group())