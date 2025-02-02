from random import randint
def usrname_generator(fullname : str)-> str:
    return fullname.split(" ")[randint(0,len(fullname.split(" "))-1)]+str(randint(0,100000))
    