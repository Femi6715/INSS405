
def request():
    num = input('Enter number')
    print(even(num))

def even(num):
   if(int(num)%2==0):
     return 'Even number'
   else:
       return 'Odd number'


request()