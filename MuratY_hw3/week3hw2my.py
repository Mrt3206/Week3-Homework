
def read_number():
    """A function that outputs the transcription of an input number with two digits.

Example:

28---------------->Twenty Eight
"""
    number=[]
    tenth={2:"Twenty", 3:"Thirty", 4:"Fourty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety",
       10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Forteen",15:"Fifteen",16:"Sixteen",17:"seventeen",
       18:"Eighteen",19:"ninetten"}
    oneth={0:" ",1:"one", 2:"two", 3:"three", 4:"four",5:"five", 6:"six", 7:"seven", 8:"eight",9:"nine"}
    str=input("Enter a number with two digits: ")
    for item in tenth.keys():
        if int(str[0])==item and item<10:
            number.append(tenth[item])
        elif int(str)==item and item>10:
            return print(tenth[item])
    for key in oneth.keys():
        if int(str[1])==key:
            number.append(oneth[key]) 
    str=" ".join(number)
    print(str)
