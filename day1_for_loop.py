#for loop examples!

#print hello world 5 times
for i in range(5):
    print("Hello World!")


#print numbers from 1 to 9
for i in range(1,10):
    print("number: ",i)

   
 #print even numbers between 1 to 20
for i in range(2,20):
    if i%2==0:
        print("even number: ",i)   

#print odd numbers between 1 to 20
for i in range(1,20):    
    if i%2!=0:
        print("odd number: ",i)


#sum of first n natural numbers
n= int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("The sum of first",n,"natural numbers is:",sum)

#factorial of a number
num= int(input("Enter a number to find its factorial: "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print("The factorial of",num,"is:",factorial)        

#multiplication table of a number
number= int(input("Enter a number to print its multiplication table: "))
print("Multiplication table of",number,":")
for i in range(1,11):
    print(number,"x",i,"=",number*i)    


#find the largest number in a list
numbers= [34, 67, 23, 89, 2, 45]
largest= numbers[0]
for num in numbers:
    if num>largest:
        largest=num   
print("The largest number in the list is:",largest)



#find the smallest number in a list
smallest= numbers[0]
for num in numbers:
    if num<smallest:
        smallest=num   
print("The smallest number in the list is:",smallest)



#count the number of vowels in a string
string= input("Enter a string: ")
vowels= "aeiouAEIOU"
count=0
for char in string:
    if char in vowels:
        count+=1
print("The number of vowels in the string is:",count)



#reverse a string
string= input("Enter a string to reverse: ")
reversed_string=""
for char in string:
    reversed_string= char + reversed_string
print("The reversed string is:",reversed_string)



#check if a number is prime
num= int(input("Enter a number to check if it is prime: "))
is_prime= True
for i in range(2,num):
    if num%i==0:
        is_prime= False
        break
if is_prime:
    print(num,"is a prime number.")
else:
    print(num,"is not a prime number.")
