#regular expression are tools for pattern matching in strings

import re
text = "The quick brown fox jumps over the lazy dog and the fox is red in color. "

#search for a pattern:
match = re.search("brown", text)
if(match):
    print("match found !")
    print("starts at : ", match.start())
    print("ends at : ", match.end())

#find all the occurences:
matches = re.findall("the", text, re.IGNORECASE)
print(matches)

#replace all the occurences of a pattern:
new_text = re.sub("fox", "cat", text)
print(new_text)

