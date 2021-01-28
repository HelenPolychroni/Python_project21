import math
a=input("Hellooo,give me a(n) (ascii) file: ")
f = open(a, "r")
data =f.read()
f.close()
print("\nYour file inside looks like this:\n\n",data)
data1= ' '.join(str(ord(c))for c in data)
#print("\ndata1 is:\n",data1)

def stringToList(string):
    listRes = list(string.split(" "))
    return listRes

l1=stringToList(data1)
#print("\nl1 is:  ",l1) # -----oi arithmoi oloi arhika type string---

l2 = [int(i) for i in l1]
#print("\nThe converted list with integers(arhikh lista) : \n",l2)

#keep only the odd numbers
l2=([i for i in l2 if i % 2 != 0])
#print("\nthe new list is:(mono oi monoi haraktires ascii):\n",l2)
#print("\nto mhkos ths listas me tous monous harakthres einai: ",len(l2))


b=len(l2)
c=[]


for j in range(b):
          x=chr(l2[j])
          c.append(x)


#print("\nthe list with characters is(the odd ones):\n",c)
#print("\nto mhkos apo harakthres ths listas me tous monous ascii einai ",len(c))

#keep only the letters
c1=([i for i in c if ((ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90))])
#print("\n c1 (monoi kai mono letters) is:\n",c1)
#print("\nto mhkos ayths einai: ",len(c1))


l3=[]
l4=[]
frequency = {}
for item in c1:
   if (item in frequency):
      frequency[item] += 1
   else:
      frequency[item] = 1
for key, value in frequency.items():
    l3.append(key)
    l4.append(value)
#print("l3 is: ",l3)
#print("\nl4 is: ",l4)
print("\nTa statistika emfanishs twn (monwn se ascii code) grammatwn einai ta parakatw:\n")
for i in range(len(l4)):
    p=(l4[i]/(len(c)))*100
    q=math.modf(p)
    if (q[0]>0):
         print(l3[i],":","*"*( (int(q[1])) + 1))
    else:
         print(l3[i],":","*"* (int(q[1]) ))
