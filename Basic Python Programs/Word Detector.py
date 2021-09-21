import os

def isDollar(filename):
    with open(filename,"r") as f:
        fileContent=f.read()
        fileContents=fileContent.lower()
        # lower() function changes the data into lowercase
        count=0
    if "dollar" in fileContents:
        count=fileContents.count("dollar")
        # count() method to get the frequency of that particular value
        return count
    else:
        print("The Word 'Dollar' is not found !!!")

if __name__=="__main__":
    dir_contents=os.listdir()
    for item in dir_contents:
        if item.endswith('txt'):
            print(f"detecting dollar in {item}")
            count=isDollar(item)
            if(count>0):
                print(f"*****Dollar found in {item}!!!!!!!")
            else:
                print(f"Dollar not found in {item}")
print("******Dollar Detector Summary*******")
print(f"{count} times of word Dollar was found")