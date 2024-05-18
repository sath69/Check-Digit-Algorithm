def splitDigits(str1):
    splitstr1=[]
    for i in str1:
        splitstr1.append(int(i))
    return splitstr1
#Main Subprogram
ccnum = input("Enter your credit card number: ")
total = 0
evenarray = []
try:
    int(ccnum)
except ValueError:
    print("Invalid Input.")
    exit()
else:
    array = splitDigits(ccnum)
    for i in range(len(array)):
      if i % 2 == 0:
        if array[i] * 2 > 9:
            doubled = array[i] * 2
            sep = splitDigits(str(doubled))
            for j in range(len(sep)):
               evenarray.append(sep[j])
        else:
            eventotal = array[i] * 2
            evenarray.append(eventotal)
      else:
        evenarray.append(array[i])

for x in range(len(evenarray)):
    total += evenarray[x]

#Credit Card Number Validation
if total % 10 == 0:
    print("Valid Credit Card Number.")
else:
    print("Invalid!")
