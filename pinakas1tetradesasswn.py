import numpy as np
a=int(input("Hey,enter desired size of the array(one number is enough): "))
while a<4:
    print("\nI am sorry,but i cannot help you with the given dimension.")
    a=int(input("Give me now a new one: "))

#fours=[]
fourAces=0
for i in range(100):
   A= np.zeros((a,a), int)
   if ((a*a)%2)!=0:
      halfarray=((a*a)//2) + 1
      #print("halfarray is: ",halfarray)
   else:
     halfarray=((a*a)//2)

   choices = np.random.choice(A.size,halfarray, replace=False)
   A.ravel()[choices]=1
   #print("Table grid looks like this:\n",A)


   #nested list below ↴
   fdiag = [[] for _ in range(2*a-1)] #to range deihnei posa tha einai ta zevgaria


   #nested list again ↴
   bdiag = [[] for _ in range(2*a-1)] #same range with fdiag
   k = -a + 1 #prokeimenou na vroume ta stoiheia ths allhs diagoneiou

   for x in range(a):
       for y in range(a):
           fdiag[x+y].append(A[y][x])
           bdiag[x-y-k].append(A[y][x])


   #print("ta stoiheia mazi me thn deuterevousa diagwnio einai:(fdiag)\n",fdiag)
   #print("ta stoiheia mazi me thn kiria diagwnio einai:(bdiag)\n",bdiag)

   f1=len(fdiag)
   #print("\nH mia diagwnios einai: ",fdiag)
   #print("\nH allh  diagwnios einai: ",bdiag)
   for i in range (0,f1):
      s=0
      l=len(fdiag[i])
      if l>=4:
          for j in range (0,l-1):
               if fdiag[i][j]==1 and fdiag[i][j+1]==1:
                     s+=1
          if s>=3:
             fourAces+=s-2
          else:
             s=0

   #print("\nOi tetrades apo assous sthn fdiag einai:\n",fourAces)



   for i in range (0,f1):
      s1=0
      l=len(bdiag[i])
      if l>=4:
          for j in range (0,l-1):
             if bdiag[i][j]==1 and bdiag[i][j+1]==1:
                 s1+=1
          if s1>=3:
             fourAces+=s1-2
          else:
               s1=0

   #print("\nOi tetrades apo assous sthn  bdiag einai:\n",fourAces)


   #gia orizontia
   for i in range (0,a):
       s2=0
       for j in range (a-1):
          if A[i][j]==1 and A[i][j+1]==1:
             s2+=1
       if s2>=3:
          fourAces+=s2-2
       else:
          s2=0 #mono oi sinehomenoi assoi
   #print("\nTetrades apo assous orizontia: ",fourAces)


   #gia katheta
   for j in range (0,a):
       s3=0
       for i in range (a-1):
          if A[i][j]==1 and A[i+1][j]==1:
            s3+=1
       if s3>=3:
          fourAces+=s3-2
       else:
            s3=0
   #print("\nTetrades apo assous katheta: ",fourAces)
#fours.append(four)
#total
print("\nSinolika oi tetrades apo 4 assous einai: ",fourAces)
#average
print("\nO mesos oros aytwn einai: ",(fourAces/100))
