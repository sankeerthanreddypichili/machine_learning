# Q1) program to count no of vowels and consonants in input string

def count(inputstring):
    vowels="aeiou"
    inputstring=inputstring.lower()
    v_count=0
    c_count=0
    for c in inputstring:
        if c.isalpha():
            if c in vowels:
                v_count+=1
            else:
                c_count+=1
    return v_count,c_count
if __name__=="__main__":
    text="Machine_learning"
    print("vowels and consonats count is :",count(text))