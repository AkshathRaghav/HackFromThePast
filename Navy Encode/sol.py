from nltk.corpus import words
word_list = words.words()

# In Hackerrank, all the words in the dictionary could not be downloaded for the 3 test cases. 
# So we have added all the words needed to decode the three test cases in a .txt file. --> word_list = [] 
 
terminate = False
space = False
 
 
inp = str(input("enter a word: "))
out = ""
 
if " " in inp: 
    space = True
if space == False:
    while terminate == False:
        for x in range(-26,27):
            for y in range(0,len(inp)):
                out += chr(ord(inp[y])+x)
            if out in word_list:
                terminate = True
                print (out)
            out = ""
 
else:
    lim = inp.index(" ")
    new_str = ""

    while terminate == False:
        for a in range(-26,27):
                for b in range(0,lim):
                    new_str += chr(ord(inp[b])+a)
                if new_str in word_list:
                    terminate = True
                    c = a


                    out = new_str
                    out += " "
                new_str = ""
    for d in range(lim+1,len(inp)):
        if inp[d] != " ":
            out += chr(ord(inp[d])+c)
        else:
            out += " "
    print (out)
