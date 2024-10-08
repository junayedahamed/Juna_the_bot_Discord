import  random

def guess_right(val):
    r_g=random.randint(1,10)
    if val ==r_g:
        return  "You won!!!"
    else:
        return " you guess the worng value"
    pass