"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# I think this will assign a list of strings to the some_words variable
some_words = ["what", "does", "this", "line", "do", "?"] #It assigned a list of strings to the some_words variable
#I think this will tell the next line of code to do something to each string in the some_words list of strings
for word in some_words:
    print(word)  #It printed each string from the some_words list
#I think this will tell the next line of code to do something to each string in the some_words list of strings
for x in some_words:
    print(x)  #it printed each string from the some_words list
# I think this will print the list of strings called some_words
print(some_words)  #It printed the list of strings called some_words
#An if statement that's telling the next line to do something if the length of the list some_words is greater than 3
if len(some_words) > 3:
    print("some_words contains more than 3 words") #It printed the phrase it was told to print if the length of some_words was greater than 3

#I think it's naming some function called usefulFunction() which will print some "named tuple" containing six attributes: system, node, release, version, machine, and processor.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

#I think this will call the function as defined above
usefulFunction() #it called the function which printed the named tuple with the 6 attributes, which appear to be specific to my computer
