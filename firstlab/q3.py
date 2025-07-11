def common(l1,l2):
    s1=set(l1)
    s2=set(l2)
    common=s1&s2
    return len(common)
if __name__=="__main__":
    list1=[1,2,3,4,5]
    list2=[4,5,6,7,8]
    print("count of common elements ",common(list1,list2)) 