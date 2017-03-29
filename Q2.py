def myCounter(n):
    mylist = []
    n = int(n)
    for i in range(1,n+1):
        if(i%15 ==0 or not(i%3==0 or i%5 ==0)):
            mylist.append(i)
    return mylist

if __name__ == "__main__":
    i = input()
    mylist = myCounter(i)
    print(len(mylist))
