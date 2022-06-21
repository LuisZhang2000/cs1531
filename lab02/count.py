

def count_char(text):
    # TODO count the number of times each character occurs in the text
    # and print out each character along with its count
    lookup = ""
    for c in text:
        if c not in lookup:
            cnt = text.count(c)
            print(c + " " + str(cnt))
            lookup = lookup + c
    pass    

def count_char_insensitive(text):
    # TODO do the same as `count_char` but in a case-insensitive manner
    lookup = ""
    for c in text.lower():
        if c.lower() not in lookup.lower():
            cnt = text.lower().count(c.lower())
            print(c.lower() + " " + str(cnt))
            lookup = lookup + c.lower()
    pass


def count_char_ordered(text):
    # TODO print the characters in the descending order of the count
    # HINT: lookup `sorted()` in the Python documentation
    
    # This task is quite difficult, so please feel free to make use of
    # resources online (Python docs, Stack Overflow, etc.)
    
    # "lookup" is the string containing characters already found
    # new characters are added to this string as they are processed
    # any characters exists in this string is skipped
    mydict = {}
    lookup = ""
    for c in text.lower():
        if c not in lookup:
            # count the number of occurrences of current character "c" within string "text"
            cnt = text.lower().count(c.lower())

            # add character and count to dictionary as key/value pair
            mydict[c.lower()] = cnt

            # new character added to lookup string 
            lookup = lookup + c
    
    # sort the items in the dictionary in descending order
    sorted_dict = sorted(mydict, key=mydict.get, reverse=True)
    
    # print all elements in the sorted dictionary
    for r in sorted_dict:
        print (r, mydict[r])
    pass
