'''FizzBuzz rules
n numbers
-if n is divisible by 3 give me Fizz
-if n is divisible by 5 give me Buzz
-if n is divisible by 3 and 5 give me FizzBuzz
-if n not in one of the other conditions give me the number'''

def divisible_5(num : int):
    if num%5 == 0:
        return True
def divisible_3(num : int):
    if num%3 == 0:
        return True

def FizzBuzz(n : int):
    num=[]
    fiz_buz=[]
    for s in range(n):
        num.append(s+1)
    for n in num:
        if divisible_5(n) and divisible_3(n):
            fiz_buz.append('FizzBuzz')
        elif divisible_3(n) :
            fiz_buz.append('Fizz')
        elif divisible_5(n) :
            fiz_buz.append('Buzz')

        else:
            fiz_buz.append(str(n))
    print(', '.join(fiz_buz))

FizzBuzz(int(input('Até que valor?\n')))


