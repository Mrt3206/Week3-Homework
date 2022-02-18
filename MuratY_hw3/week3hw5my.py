def equal_reverse(s):
    """A function that controls the given
    inputs whether they are equal to their reversed order or not.
Example:
Input  >>> madam, tacocat, utrecht 

Output >>> True, True, False"""

    for i in s.split(", "):                      # A list consists of words
            i_list=list(i)                       # Take each word by letter
            i_list=[x for x in i_list if x!=" "] 
            i_list.reverse()                     #reverse order of letter
            i_reverse= "".join(i_list)           # word again by reverse order
            if i==i_reverse:                     # compare words are equal
                s=s.replace(i,"True")            # write truw or false
            else:
                s=s.replace(i,"False")
       
    return s