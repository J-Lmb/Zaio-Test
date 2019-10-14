my_range = int(input("Enter your range number: "))

value1, value2 = 0, 1
           
for i in range(0, my_range):
   if(i <= 1):
      nxt = i
   else:
      nxt = value1 + value2
      value1, value2 = value2, nxt
    
   print(nxt,end="")
   if i != my_range-1:
      print( ", ",end="" )