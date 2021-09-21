import string
import random
from gibberish_detector import detector
if __name__=="__main__":
    s1=string.ascii_lowercase
    # print(s1)
    s2=string.ascii_uppercase
    # print(s2)
    s3=string.digits
    # print(s3)
    s4=string.punctuation
    # print(s4)
    detector=input("Enter Password Length\n")
    detect=detector.isnumeric()
    if detect is True:
        plen=int(detector)
        s=[]
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        # print(s)
        random.shuffle(s)
        # print(s)
        print("Your Password is :")
        print("".join(s[0:plen]))
        print("".join(random.sample(s,plen)))
    else:
        print("Please enter a number.")

    