import random

special = ['!','@','#',"$",'$','%','^','&','*',"(",')',":",".",',',"<>","/",'{',"}","~"]

num = ["1","2","3","4","5","6","7","8","9","0"]

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

list1 = []

list2 = []

str1 = ''

str2 = ''

password_strength = input("HI IAM PASSWORD GENERATOR DO YOU NEED A STRONG OR WEAK PASSWORD (S/W)>>>  ")

if password_strength.lower() == "s" :

    for i in range(1,10):

        list1.append(random.choice(special))

    for j in range(1,10):

        list1.append(random.choice(num))

    for k in range(1,10):

        list1.append(random.choice(char))

for x in list1 :

    str1 = str1 + str(x)

if password_strength.lower() == "w" :

    for q in range(1,5):

        list2.append(random.choice(special))

    for w in range(1,5):

        list2.append(random.choice(num))

    for c in range(1,5):

        list2.append(random.choice(char))

for y in list2 :

    str2 = str2 + str(y)

if str1 == '':

    print("YOUR PASSWORD IS READY >>>",str2)

elif str2 == '':

    print("YOUR strong PASSWORD IS READY >>>",str1)