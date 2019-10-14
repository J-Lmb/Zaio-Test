s = input("Please enter a word or sentence: ")

print ("The entered string  is : ", s)   

def reverse(input): 
  string = "" 
  for i in input: 
    string = i + string
  return string

print ("The reversed string is : ",reverse(s))