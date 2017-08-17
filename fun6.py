def add(x,y):
    sum=x+y
    return sum
num1=5
num2=6
    
print (add(num1,num2))

def greet(name,msg):
    print('hello',name+','+msg)
greet('hai','good morning')

def greet(name, msg = "Good morning!"):
   """
   This function greets to
   the person with the
   provided message.

   If message is not provided,
   it defaults to "Good
   morning!"
   """

   print("Hello",name + ', ' + msg)

greet("Kate")
greet("Bruce","How do you do?")
    
def greet(*names):
   """This function greets all
   the person in the names tuple."""

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")

def fun(*names):
    for name in names:
        print('hello',name)
fun('as','sd','fgh')
