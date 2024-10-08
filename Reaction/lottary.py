import random

def who_is_winnner(lp):
    print(len(lp))
    print(lp)
    if(type(lp) is not list):
        return
    else:
        val=random.randint(0,len(lp)-1)
        return lp[val]