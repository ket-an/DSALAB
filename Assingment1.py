#Hashtable class which defines the size of hashtable to 20 and initializing hashtable with -1..
class Hashtable:
    Table_size=20
    current_size=0
    #initializing hashtable with -1
    hashtable=[-1]*Table_size


#creating an object of Hashing class
h = Hashtable()


#hash1() is the hash function which is applied on each key..
def hash1(k):
    return k % h.Table_size


#hash2() is the second hash function for double hashing..
def hash2(k):
    return k % 13


#method for linear probing without replacement..
def withoutreplacement(key):
    index=hash1(key)

    if h.hashtable[index]==-1:
            h.hashtable[index]=key
            h.current_size=h.current_size+1
    else:
            while h.hashtable[index]!=-1:
                index=index+1
                if h.hashtable[index]==-1:
                    break
                elif index==h.Table_size-1:
                    index=0
                    continue
                else:
                    continue

            h.hashtable[index]=key
            h.current_size=h.current_size+1
#ending of withoutreplacement() method..


#method for linear probing with replacement..
def withreplacement(key):
    index=hash1(key)

    if h.hashtable[index]==-1:
        h.hashtable[index]=key
        h.current_size=h.current_size+1
    else:
        index=index+1
        h.hashtable[index]=key
        h.current_size=h.current_size+1
#ending of withreplacement() method..


#method for linear probing using double hashing..
def doublehashing(key):
    for i in range(0,h.Table_size):
        index=(hash1(key)+i*hash2(key))%h.Table_size

        if h.hashtable[index]==-1:
            h.hashtable[index]=key
            h.current_size=h.current_size+1
            break
        else:
            continue
#ending of doublehashing() method..


#main method..
def main():
    list=[]
    n=int(input("Enter the number of keys: "))
    print("Enter the values of keys: ")
    for i in range(0,n):
        element=int(input())
        list.append(element)

    choice=int(input("1.Linear Probing With replacement\n2.Linear Probing Without replacement\n3.Double Hashing\nEnter Your choice: "))
    if choice==1:
        for i in range(0,n):
            withreplacement(list[i])

    if choice==2:
        for i in range(0,n):
            withoutreplacement(list[i])

    if choice==3:
        for i in range(0,n):
            doublehashing(list[i])

    print("Key's values are:")
    print(list)
#ending of main method..


#call to the main method..
main()

#printing hashtable's value..
print(h.hashtable)










