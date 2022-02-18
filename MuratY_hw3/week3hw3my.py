
def alphabetical_order(s):
    """Afunction that takes an input
    of different words with hyphen (-)
    in between them and then:

sorts the words in alphabetical order,
adds hyphen icon (-) between them,
gives the output of the sorted words.
Example:

Input  >>> green-red-yellow-black-white

Output >>> black-green-red-white-yellow """
    
    return "-".join(sorted(s.split("-"))) #All word without hypen takes in list then sorted and again joining.

