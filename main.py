name = 'hadi'
age = 15

if age == 15 and name == 'hadi':
    print('your name is hadi and your age is 15')
    if name == 'ali' or name == 'hadi':
        print('your name is either hadi or rick')



astring = 'hello world'

print('\nthe amount of letter L in hello world : ', astring.count('l'))
print('this is the hello world with capital letters : ', astring.upper())
print('\nthis is the reverse of the hello world : ', astring[::-1])
print('\nyea baby this is : ', astring.startswith('hello'))
print('this is a real thing but unfortunatly this is : ', astring.endswith('emame kooni'))


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('\nthis is the smallest number :', min(number))
print('this is the biggest number :', max(number))
print('\n!= means it isnt but == means it is :', max(number) != 10)
print('and also this :', min(number) > 5)

my_list = [1, 2, 3, 4, 5, 6, 7, 18, 19 ,16]

my_list_has_10 = 10 in my_list

print('\nit says if i have 10 in my_list or not, wich is :', my_list_has_10)

print('\nthis will prints out the numbers in my_list above the number 3')
for item in my_list:
    if item > 3:
        print(item)

new_list = [1, 2, 6, 1, 5, 3, 2, 6, 1, 6, 5, 2, 5, 4, 3, 4, 3, 4]
new_list.sort()

print('\nit sorts the numbers in new_list from smallest to biggest number :')
print(new_list)

the_new_list = set(new_list)

print('\nthis will deduplicates the numbers :')
print(the_new_list)

# here is an example for functions . the return is just like the print

def asghar(x):
    return 2 * x

a = asghar(3)

print('\nthis is the output :', a)

# more examples

def function1(x, z):
    return x + z

b = function1(2, 5)

print('\nthis is the output fnc1 :', b)

def function2(some_arg):
    print('\n', some_arg)
    print('hoy haa amrica pedasag')

function2(4)

# BMI calculator

name1 = "asghar"
height_m1 = 1.8
weight_kg1 = 60

name2 = "asghar's brother"
height_m2 = 2
weight_kg2  = 72

name3 = "asghar's sister"
height_m3 = 1.7
weight_kg3 = 120

def bmi_calculation(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("\nbmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not over weight"
    else :
        return name + " is over weight"

result1 = bmi_calculation(name1, height_m1, weight_kg1)
result2 = bmi_calculation(name2, height_m2, weight_kg2)
result3 = bmi_calculation(name3, height_m3, weight_kg3)

print("\n")
print(result1)
print(result2)
print(result3)

"""
lets find a soloution for this

"""



