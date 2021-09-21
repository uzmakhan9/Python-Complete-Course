# explaining of if __name__=="__main__" 

import os
# importing os module for the illustration

def someFunction():
    print("uzma will become a good software engineer one day.")

print(__name__)
'''this statement gives __main__ as the output, that means the value of __name__ is __main__ in this file
because it directly calls from its main file but the value of __name__ changes when we called it by import,
its value changes from __main__ to that file name from which we import it'''

if(__name__=="__main__"):
    print(os.listdir("/"))
    print("uzma is a good coder.")
